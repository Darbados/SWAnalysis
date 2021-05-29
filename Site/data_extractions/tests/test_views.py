from django.test.testcases import TestCase
from django.test import Client
from django.urls import reverse


class DataCollectorsViewsTests(TestCase):
    def setUp(self):
        super().setUp()

        self.client = Client()

    def test_exports_get_success(self):
        """ Test exports page is loaded successfully, with no exports in DB. """

        response = self.client.get(reverse('data_extractions:exports'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['extractions'].number, 1)
