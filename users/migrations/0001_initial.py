# Generated by Django 4.0.4 on 2022-09-04 10:43

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('avatar', models.ImageField(blank=True, upload_to='users/%Y/%m/%d/')),
                ('default_avatar', models.CharField(default='https://res.cloudinary.com/iamalmiir/image/upload/v1657350671/catAvatar_iakq5p.jpg', max_length=255)),
                ('email', models.EmailField(max_length=50, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=15, unique=True, verbose_name='user name')),
                ('full_name', models.CharField(max_length=100, verbose_name='full name')),
                ('photo', models.ImageField(blank=True, upload_to='', verbose_name='profile picture')),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='start date')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
