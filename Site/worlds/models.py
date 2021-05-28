from django.db import models
from Site.mixins import TimeStampMixin


class Planet(TimeStampMixin):
    climate = models.CharField(max_length=64)
    diameter = models.DecimalField(max_digits=15, decimal_places=3)
    gravity = models.CharField(max_length=32)
    name = models.CharField(max_length=128)
    orbital_period = models.IntegerField()
    population = models.IntegerField()
    rotation_period = models.IntegerField()
    surface_water = models.BooleanField(default=False)
    terrain = models.CharField(max_length=32)
    url = models.URLField()

    def __str__(self):
        return self.name
