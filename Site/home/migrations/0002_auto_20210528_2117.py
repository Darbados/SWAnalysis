# Generated by Django 3.1.8 on 2021-05-28 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analystuser',
            name='created_at',
            field=models.DateTimeField(db_index=True),
        ),
    ]
