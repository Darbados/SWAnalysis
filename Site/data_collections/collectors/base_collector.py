from urllib.parse import urlparse, parse_qs, urljoin

import requests


class ResponseAPIUrlException(Exception):
    pass


class BaseDataCollector:
    """
    Simple data collector that fetch the data from RESOURCE_URL consequently for all the
    pages for the given API.
    """

    BASE_API_URL = 'https://swapi.dev/api/'
    RESOURCE_API_URL = None
    RESPONSE_TIMEOUT = 5

    def __init__(self):
        self.results = []

    def _fetch_data(self, page=1):
        """
        Method used to fetch the data for a given page of the requested API.

        Arguments:
            page (int): We start from page #1. Indicate the current page we try to fetch.

        Returns:
            next_page (int): The next page that we can request to fetch.
            None: If there are no other pages to request.
        """

        url = urljoin(self.BASE_API_URL, self.RESOURCE_API_URL)
        response = requests.get(url, params={'page': page}, timeout=self.RESPONSE_TIMEOUT)
        response.raise_for_status()

        if response.status_code != 200:
            return None

        response_json = response.json()
        self.results.extend(response_json['results'])
        if response_json['next'] is not None:
            next_page_url_parsed = urlparse(response_json['next'])
            return parse_qs(next_page_url_parsed.query)['page']

    def collect(self, page=1):
        if self.RESOURCE_API_URL is None:
            raise ResponseAPIUrlException('RESOURCE_API_URL must be set!')

        next_page = self._fetch_data(page)
        if next_page:
            # We need to request every page of the resource API to collect all data
            return self.collect(next_page)
        return self
