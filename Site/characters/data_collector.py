from urllib.parse import urlparse, parse_qs

import requests


class CharactersDataCollector:
    RESOURCE_URL = 'https://swapi.dev/api/people/'

    def __init__(self):
        self.results = []

    def _get_data(self, page=1):
        response = requests.get(self.RESOURCE_URL, params={'page': page})
        response.raise_for_status()

        if response.status_code == 200:
            response_json = response.json()
            if response_json['next'] is not None:
                print(response_json['next'])
                next_page_url_parsed = urlparse(response_json['next'])
                self.results.extend(response_json['results'])
                return parse_qs(next_page_url_parsed.query)['page']
        else:
            return None

    def collect(self, page=1):
        next_page = self._get_data(page)
        if next_page:
            # We need to request every page of the /people/ API to collect all people data
            return self.collect(next_page)
