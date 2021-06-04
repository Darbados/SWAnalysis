# Generated by Django 3.1.8 on 2021-06-04 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='analystuser',
            name='is_staff',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='analystuser',
            name='is_superuser',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='analystuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]