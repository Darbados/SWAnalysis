from unittest import TestCase

from AnalysisBase.templatetags.analysis_filters import add_get_params


class AnalysisFiltersTests(TestCase):
    def test_add_get_params(self):
        """ Test that add_get_params construct url and get params as expected. """

        test_urls = {
            'https://www.example.com': {
                'a': 1,
                'b': 2,
                'c': 3,
                'result': 'https://www.example.com?a=1&b=2&c=3',
            },
            'https://www.example1.com': {
                'result': 'https://www.example1.com',
            },
        }

        for url, url_params in test_urls.items():
            result_url = url_params.pop('result')
            self.assertEqual(add_get_params(url, **url_params), result_url)
