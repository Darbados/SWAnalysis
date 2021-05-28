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

    export = models.FileField(upload_to='collections_exports/')
    collection_type = models.IntegerField(choices=COLLECTION_CHOICES, db_index=True)

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
