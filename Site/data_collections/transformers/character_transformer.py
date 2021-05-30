from datetime import datetime

from data_collections.transformers.base_transformer import BaseDataTransformer


class CharacterDataTransformer(BaseDataTransformer):
    def transform_data(self, **kwargs):
        for data in self.data:
            self._transform_home_world(data, kwargs['worlds_data'])
            self._transform_edited(data)

    @staticmethod
    def _transform_edited(data):
        if 'edited' not in data:
            return
        try:
            data['date'] = datetime.strptime(data['edited'], '%Y-%m-%dT%H:%M:%S.%fZ').date()
        except ValueError:
            data['date'] = data['edited']
        del data['edited']

    @staticmethod
    def _transform_home_world(data, home_worlds):
        if 'homeworld' not in data:
            return
        data['homeworld'] = home_worlds[data['homeworld']]
