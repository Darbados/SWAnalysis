from django.db import models

from Site.mixins import TimeStampMixin


class Character(TimeStampMixin):
    EXPORT_FIELDS = [
        'name', 'height', 'mass', 'hair_color', 'eye_color', 'birth_year', 'gender', 'edited']

    GENDER_MALE = 1
    GENDER_FEMALE = 2
    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )

    name = models.CharField(max_length=128)
    height = models.IntegerField()
    mass = models.DecimalField(max_digits=5, decimal_places=2)
    hair_color = models.CharField(max_length=32)
    eye_color = models.CharField(max_length=32)
    birth_year = models.CharField(max_length=10)
    gender = models.IntegerField(choices=GENDER_CHOICES)
    url = models.URLField()
    # Person character should have only one home world.
    home_world = models.OneToOneField(
        'worlds.Planet', on_delete=models.PROTECT, related_name='characters')

