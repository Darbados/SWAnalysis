# Generated by Django 3.1.8 on 2021-05-29 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worlds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planet',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='planet',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
