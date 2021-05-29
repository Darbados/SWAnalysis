from urllib.parse import urlparse, parse_qs, urljoin

import requests


class BaseDataCollector:
    """
    Simple data collector that fetch the data from RESOURCE_URL concequently for all the
    pages for the given API.
    """

    BASE_API_URL = 'https://swapi.dev/api/'
    RESOURCE_API_URL = None
    RESPONSE_TIMEOUT = 5

    def __init__(self):
        self.results = []

    def _fetch_data(self, page=1):
        url = urljoin(self.BASE_API_URL, self.RESOURCE_API_URL)
        response = requests.get(url, params={'page': page}, timeout=self.RESPONSE_TIMEOUT)
        response.raise_for_status()

        if response.status_code == 200:
            response_json = response.json()
            self.results.extend(response_json['results'])
            if response_json['next'] is not None:
                next_page_url_parsed = urlparse(response_json['next'])
                return parse_qs(next_page_url_parsed.query)['page']
        else:
            return None

    def collect(self, page=1):
        next_page = self._fetch_data(page)
        if next_page:
            # We need to request every page of the resource API to collect all data
            return self.collect(next_page)
