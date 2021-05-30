# Generated by Django 3.1.8 on 2021-05-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DataCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('export', models.FileField(upload_to='collections/')),
                ('collection_type', models.IntegerField(choices=[(1, 'Characters'), (2, 'Worlds')], db_index=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
