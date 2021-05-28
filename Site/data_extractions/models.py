from django.db import models

from Site.mixins import TimeStampMixin


class DataExport(TimeStampMixin):
    COLLECTION_CHARACTERS = 1
    COLLECTION_WORLDS = 2
    COLLECTION_CHOICES = (
        (COLLECTION_CHARACTERS, 'Characters'),
        (COLLECTION_WORLDS, 'Worlds'),
    )

    export = models.FileField(upload_to='collections_exports/')
    collection_type = models.IntegerField(choices=COLLECTION_CHOICES, db_index=True)
