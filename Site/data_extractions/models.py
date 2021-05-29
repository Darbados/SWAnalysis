import csv
import io

from django.core.files.base import ContentFile
from django.db import models

from Site.mixins import TimeStampMixin
from characters.models import Character
from data_extractions.utils import transform_name, transform_field_data


class DataExport(TimeStampMixin):
    COLLECTION_CHARACTERS = 1
    COLLECTION_WORLDS = 2
    COLLECTION_CHOICES = (
        (COLLECTION_CHARACTERS, 'Characters'),
        (COLLECTION_WORLDS, 'Worlds'),
    )
    DEFAULT_ROWS_TO_DISPLAY = 10

    export = models.FileField(upload_to='collections_exports/')
    collection_type = models.IntegerField(choices=COLLECTION_CHOICES, db_index=True)

    @property
    def export_name(self):
        return self.export.name.split('/')[-1]

    def get_rows_to_display(self, rows_multiplier):
        rows_count = 0
        with open(self.export.path, 'r') as source:
            reader = csv.reader(source)

            for row in reader:
                if row[0] == 'name':
                    continue

                if rows_count < self.DEFAULT_ROWS_TO_DISPLAY * rows_multiplier:
                    yield row
                    rows_count += 1

    @classmethod
    def create_from_fetched_data(cls, data):
        contents = io.StringIO()
        writer = csv.writer(contents)

        writer.writerow([transform_name(field) for field in Character.EXPORT_FIELDS])

        for hero_data in data:
            writer.writerow([
                transform_field_data(field, hero_data.get(field)) for field in
                Character.EXPORT_FIELDS])

        cls.objects.create(
            export=ContentFile(contents.getvalue(), name='people_collection.csv'),
            collection_type=cls.COLLECTION_CHARACTERS,
        )

    class Meta:
        ordering = ('-created_at',)
