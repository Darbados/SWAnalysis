from data_extractions.collectors.base_collector import BaseDataCollector


class _WorldsDataCollector(BaseDataCollector):
    RESOURCE_API_URL = 'planets/'


WorldsDataCollector = _WorldsDataCollector
