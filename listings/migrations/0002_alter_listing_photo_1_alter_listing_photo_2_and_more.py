# Generated by Django 4.1.4 on 2023-01-08 21:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("listings", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="listing",
            name="photo_1",
            field=models.ImageField(
                blank=True, upload_to="ar-realty/listings/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="photo_2",
            field=models.ImageField(
                blank=True, upload_to="ar-realty/listings/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="photo_3",
            field=models.ImageField(
                blank=True, upload_to="ar-realty/listings/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="photo_4",
            field=models.ImageField(
                blank=True, upload_to="ar-realty/listings/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="photo_5",
            field=models.ImageField(
                blank=True, upload_to="ar-realty/listings/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="photo_main",
            field=models.ImageField(
                blank=True, upload_to="ar-realty/listings/%Y/%m/%d/"
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="pub_date",
            field=models.DateTimeField(
                blank=True, default=datetime.datetime(2023, 1, 8, 16, 30, 21, 795463)
            ),
        ),
        migrations.AlterField(
            model_name="listing",
            name="year_built",
            field=models.IntegerField(default=2023),
        ),
    ]
