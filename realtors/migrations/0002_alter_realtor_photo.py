# Generated by Django 4.1.4 on 2023-01-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("realtors", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="realtor",
            name="photo",
            field=models.ImageField(blank=True, upload_to="ar/realtors/%Y/%m/%d/"),
        ),
    ]
