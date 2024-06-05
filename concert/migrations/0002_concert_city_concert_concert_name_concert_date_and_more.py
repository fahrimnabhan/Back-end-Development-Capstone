# Generated by Django 4.2.13 on 2024-06-04 03:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("concert", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="concert",
            name="city",
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="concert",
            name="concert_name",
            field=models.CharField(max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="concert",
            name="date",
            field=models.DateField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name="concert",
            name="duration",
            field=models.IntegerField(),
            preserve_default=False,
        ),
    ]
