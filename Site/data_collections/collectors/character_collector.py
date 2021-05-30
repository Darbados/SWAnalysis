from data_collections.collectors.base_collector import BaseDataCollector


class _CharactersDataCollector(BaseDataCollector):
    RESOURCE_API_URL = 'people/'


CharacterDataCollector = _CharactersDataCollector
