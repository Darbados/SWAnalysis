import os

from django.db import models
from django.dispatch import receiver

from data_collections.models import DataCollection


@receiver(models.signals.pre_delete, sender=DataCollection)
def auto_delete_collection_file_on_collection_delete(sender, instance, **kwargs):
    if instance.file:
        path = instance.file.path
        if os.path.isfile(path):
            try:
                os.remove(path)
            except Exception:
                pass
