# Generated by Django 4.1.4 on 2023-01-08 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_remove_user_photo_alter_user_avatar_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.ImageField(blank=True, upload_to="ar/users/avatar/%Y/%m/%d/"),
        ),
    ]
