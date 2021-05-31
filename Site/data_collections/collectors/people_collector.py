from data_collections.collectors.base_collector import BaseDataCollector


class _PeopleDataCollector(BaseDataCollector):
    RESOURCE_API_URL = 'people/'


PeopleDataCollector = _PeopleDataCollector
