# Generated by Django 4.1.4 on 2023-01-08 21:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0002_alter_listing_photo_1_alter_listing_photo_2_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="pub_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 1, 8, 16, 34, 52, 781833)
            ),
        ),
    ]