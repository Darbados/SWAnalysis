from datetime import date
from unittest import TestCase
from data_collections.transformers.tests.helpers import people_data
from data_collections.transformers.character_transformer import PeopleDataTransformer


class CharacterDataTransformerTests(TestCase):
    def test_transform_data(self):
        """ Test CharacterDataTransformer transforms data correctly """

        # No homeworld transformation here
        ch_transformer = PeopleDataTransformer(people_data)
        ch_transformer.transform_data()

        for data_result in ch_transformer.data:
            with self.subTest(name=data_result['name']):
                self.assertEqual(data_result['date'], date(2014, 12, 20))

        # Transform both homeworld and edited columns
        ch_transformer = PeopleDataTransformer(people_data)
        ch_transformer.transform_data(worlds_data={'http://swapi.dev/api/planets/1/': 'Tatooine'})

        for data_result in ch_transformer.data:
            with self.subTest(name=data_result['name']):
                self.assertEqual(data_result['date'], date(2014, 12, 20))
                self.assertEqual(data_result['homeworld'], 'Tatooine')
