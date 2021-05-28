import csv
from datetime import datetime

from characters.models import Character

_ISO_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


def transform_name(field_name):
    """
    The column edited should be displayed as date, so once we're on it,
    we transform the name.

    Arguments:
        field_name (str): Current field name

    Return:
        str: Either the original field_name or the transformed version of it.
    """

    if field_name != 'edited':
        return field_name
    return 'date'


def transform_field_data(field_name, field_data):
    """
    The column edited value should be displayed as date, so once we're on it,
    we'll try to covert it to date.

    Arguments:
        field_name (str): Current field name
        field_data (str): Current field value

    Return:
        str: Either the original field_data or the transformed version of it.
    """

    if field_name != 'edited':
        return field_data
    try:
        return datetime.strptime(field_data, _ISO_FORMAT).date()
    except ValueError:
        return None


def create_csv_writer(writer, data):
    writer.writerow(transform_name(field) for field in Character.EXPORT_FIELDS)

    for hero_data in data:
        writer.writerow([
            transform_field_data(field, hero_data.get(field)) for field in Character.EXPORT_FIELDS])

    return writer
