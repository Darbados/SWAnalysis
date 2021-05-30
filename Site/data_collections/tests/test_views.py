from django.core.files.base import ContentFile
from django.test.testcases import TestCase
from django.test import Client
from django.urls import reverse

from AnalysisBase.templatetags.analysis_filters import add_get_params
from data_collections.models import DataCollection
from data_collections.tests.helper_data import collection_data


def _create_collections(count):
    for _ in range(count):
        DataCollection.objects.create(
            file=ContentFile(collection_data, 'peopple_collection'),
            collection_type=DataCollection.COLLECTION_CHARACTERS,
        )


class DataCollectionsViewsTests(TestCase):
    def setUp(self):
        super().setUp()

        self.client = Client()

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

    def test_value_counts_get_success(self):
        """ Test value_counts collection page is successfully loaded. """

        _create_collections(1)
        collection = DataCollection.objects.first()

        url = add_get_params(
            reverse('data_collections:inspect', args=(collection.id,)),
            gender='on',
            homeworld='on',
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
