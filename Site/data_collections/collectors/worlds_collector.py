from data_collections.collectors.base_collector import BaseDataCollector


class _WorldsDataCollector(BaseDataCollector):
    RESOURCE_API_URL = 'planets/'

    def get_url_name_dict(self):
        return {
            p['url']: p['name']
            for p in self.results
        }


WorldsDataCollector = _WorldsDataCollector
