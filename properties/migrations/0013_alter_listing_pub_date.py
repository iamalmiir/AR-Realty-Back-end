# Generated by Django 4.0.1 on 2022-09-03 00:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_alter_listing_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 2, 19, 13, 59, 49289)),
        ),
    ]
