import csv
import io

from django.core.files.base import ContentFile
from django.db import models

from AnalysisBase.mixins import TimeStampMixin
from people.models import Person


class DataCollection(TimeStampMixin):
    COLLECTION_PEOPLE = 1
    COLLECTION_WORLDS = 2
    COLLECTION_CHOICES = (
        (COLLECTION_PEOPLE, 'People'),
        (COLLECTION_WORLDS, 'Worlds'),
    )
    DEFAULT_ROWS_TO_DISPLAY = 10

    file = models.FileField(upload_to='collections/')
    collection_type = models.IntegerField(choices=COLLECTION_CHOICES, db_index=True)

    @property
    def collection_file_name(self):
        return self.file.name.split('/')[-1]

    @classmethod
    def create_from_fetched_data(cls, data):
        """
        Created DataExport will be stored as a source file. Any transformation will be done
        over it to follow the concept source --> derivatives.
        """

        if not data:
            return

        contents = io.StringIO()
        writer = csv.writer(contents)

        # Write the header row
        writer.writerow(Person.EXPORT_FIELDS)
        for hero_data in data:
            writer.writerow([hero_data.get(field) for field in Person.EXPORT_FIELDS])

        cls.objects.create(
            file=ContentFile(contents.getvalue(), name='people_collection.csv'),
            collection_type=cls.COLLECTION_PEOPLE,
        )

    class Meta:
        ordering = ('-created_at',)
