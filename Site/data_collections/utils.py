import petl

from data_collections.models import DataCollection


def get_rows_to_display(table_data, rows_multiplier):
    # First row is always the header, so we slice it out of the rows slice
    return petl.rowslice(table_data, DataCollection.DEFAULT_ROWS_TO_DISPLAY * rows_multiplier)[1:]
