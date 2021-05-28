from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(db_index=True)
    updated_at = models.DateTimeField()

    # Refactor this to save values

    class Meta:
        abstract = True
