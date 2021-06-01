# Generated by Django 3.1.8 on 2021-06-01 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=128)),
                ('height', models.CharField(max_length=32)),
                ('mass', models.CharField(max_length=32)),
                ('hair_color', models.CharField(max_length=32)),
                ('skin_color', models.CharField(max_length=32)),
                ('eye_color', models.CharField(max_length=32)),
                ('birth_year', models.CharField(max_length=10)),
                ('gender', models.CharField(max_length=10)),
                ('url', models.URLField()),
                ('home_world', models.CharField(max_length=64)),
                ('edited', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
