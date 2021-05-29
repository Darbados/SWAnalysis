from urllib import parse

from django import template

register = template.Library()


@register.simple_tag
def add_get_params(url, **kwargs):
    parsed_url = list(parse.urlparse(url))
    parsed_query = parse.parse_qs(parsed_url[4])
    for key, value in kwargs.items():
        if not isinstance(value, list):
            parsed_query[key] = [value]
        else:
            parsed_query[key] = value
    parsed_url[4] = parse.urlencode(parsed_query, doseq=True)
    return parse.urlunparse(parsed_url)
