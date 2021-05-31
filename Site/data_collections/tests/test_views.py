import petl
import responses

from django.core.files.base import ContentFile
from django.test.testcases import TestCase
from django.test import Client
from django.urls import reverse

from AnalysisBase.templatetags.analysis_filters import add_get_params
from data_collections.models import DataCollection
from data_collections.tests.helper_data import collection_data, people_response, planets_response


def _create_collections(count):
    for _ in range(count):
        DataCollection.objects.create(
            file=ContentFile(collection_data, 'peopple_collection.csv'),
            collection_type=DataCollection.COLLECTION_PEOPLE,
        )


class DataCollectionsViewsTests(TestCase):
    def setUp(self):
        super().setUp()

        self.client = Client()

    @responses.activate
    def test_save_collection_post_success(self):
        """ Test save_collection view fetch and save collection data. """

        self.assertEqual(DataCollection.objects.count(), 0)
        responses.add(
            responses.GET, 'https://swapi.dev/api/people/', json=people_response, status=200)
        responses.add(
            responses.GET, 'https://swapi.dev/api/planets/', json=planets_response, status=200)
        response = self.client.post(reverse('data_collections:save_collection_data'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(DataCollection.objects.count(), 1)

        # Check actual collection
        collection = DataCollection.objects.first()
        self.assertEqual(
            [row for row in petl.fromcsv(collection.file.path)],
            [
                ('name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color',
                 'birth_year', 'gender', 'homeworld', 'date'),
                ('Luke Skywalker', '172', '77', 'blond', 'fair', 'blue', '19BBY', 'male',
                 'Tatooine', '2014-12-20'),
                ('C-3PO', '167', '75', 'n/a', 'gold', 'yellow', '112BBY', 'n/a', 'Tatooine',
                 '2014-12-20'),
            ],
        )

    def test_empty_index_get_success(self):
        """ Test collections page is loaded successfully, with no exports in DB. """

        response = self.client.get(reverse('data_collections:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['collections'].number, 1)

    def test_index_get_success(self):
        """ Test collections page is loaded successfully, with existing collections in DB. """

        _create_collections(5)

        self.assertEqual(DataCollection.objects.count(), 5)
        response = self.client.get(reverse('data_collections:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['collections'].number, 1)

    def test_inspect_get_success(self):
        """ Test inspect collection is successfully loaded. """

        _create_collections(1)
        collection = DataCollection.objects.first()

        response = self.client.get(reverse('data_collections:inspect', args=(collection.id,)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['multiplier'], 2)
        self.assertEqual(
            response.context['table_header'],
            (
                'name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color',
                'birth_year', 'gender', 'homeworld', 'date',
            ),
        )

    def test_inspect_redirects_for_not_existing_collection(self):
        """ Test inspect view redirects against not existing collection. """

        response = self.client.get(reverse('data_collections:inspect', args=(400,)))
        self.assertEqual(response.status_code, 302)

    def test_value_counts_get_success(self):
        """ Test value_counts collection page is successfully loaded. """

        _create_collections(1)
        collection = DataCollection.objects.first()

        url = add_get_params(
            reverse('data_collections:value_counts', args=(collection.id,)),
            gender='on',
            homeworld='on',
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            [row for row in response.context['value_counts_data']],
            [
                ('gender', 'homeworld', 'count'),
                ('male', 'Tatooine', 4),
                ('n/a', 'Tatooine', 2),
                ('n/a', 'Naboo', 1),
                ('female', 'Alderaan', 1),
                ('female', 'Tatooine', 1),
            ]
        )

    def test_delete_post_success(self):
        """ Test delete collection page. """

        _create_collections(1)
        collection = DataCollection.objects.first()
        collection_id = collection.id
        response = self.client.post(reverse('data_collections:delete', args=(collection_id,)))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(DataCollection.objects.filter(id=collection_id).exists())
