from django.db import models


class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(db_index=True)
    updated_at = models.DateTimeField()

    class Meta:
        abstract = True
