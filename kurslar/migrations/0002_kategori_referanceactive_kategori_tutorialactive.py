# Generated by Django 4.2.5 on 2023-10-03 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kurslar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategori',
            name='referanceActive',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='kategori',
            name='tutorialActive',
            field=models.BooleanField(default=True),
        ),
    ]
