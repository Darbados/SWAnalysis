import responses

from django.test.testcases import TestCase
from django.test import Client
from django.urls import reverse

from data_collections.tests.helper_data import people_response, planets_response
from people.models import Person


class PeopleViewsTests(TestCase):
    def setUp(self):
        super().setUp()

        self.client = Client()

    def test_index_get_success(self):
        """ Test people index page successfully loads. """

        response = self.client.get(reverse('people:index'))
        self.assertEqual(response.status_code, 200)

    @responses.activate
    def test_save_people_post_success(self):
        """ Test people fetch page works as expected. """

        responses.add(
            responses.GET, 'https://swapi.dev/api/people/', json=people_response, status=200)
        responses.add(
            responses.GET, 'https://swapi.dev/api/planets/', json=planets_response, status=200)

        response = self.client.post(reverse('people:save_people'))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Person.objects.count(), len(people_response['results']))
