from django.db import models

from AnalysisBase.mixins import TimeStampMixin


class Person(TimeStampMixin):
    EXPORT_FIELDS = [
        'name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color',
        'birth_year', 'gender', 'homeworld', 'date',
    ]

    name = models.CharField(max_length=128)
    height = models.CharField(max_length=32)
    mass = models.CharField(max_length=32)
    hair_color = models.CharField(max_length=32)
    skin_color = models.CharField(max_length=32)
    eye_color = models.CharField(max_length=32)
    birth_year = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    url = models.URLField()
    # Person character should have only one home world.
    home_world = models.ForeignKey(
        'worlds.Planet', on_delete=models.PROTECT, related_name='people', null=True)
    edited = models.DateTimeField()

    def __str__(self):
        return self.name

    @classmethod
    def create_from_fetched_data(cls, data):
        # Clear all records to avoid more heavy update logic.
        cls.objects.all().delete()

        cls.objects.bulk_create([
            cls(
                name=person_data['name'],
                height=person_data['height'],
                mass=person_data['mass'],
                hair_color=person_data['hair_color'],
                skin_color=person_data['skin_color'],
                eye_color=person_data['eye_color'],
                birth_year=person_data['birth_year'],
                gender=person_data['gender'],
                url=person_data['url'],
                edited=person_data['edited'],
            )
            for person_data in data
        ])
