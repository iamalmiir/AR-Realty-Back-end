# Generated by Django 4.0.4 on 2022-09-04 10:43

import datetime
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, editable=False, null=True, unique=True)),
                ('title', models.CharField(max_length=70)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(choices=[('AL', 'Alabama'), ('AK', 'Alaska'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PA', 'Pennsylvania'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')], max_length=2)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('garage', models.IntegerField(default=0)),
                ('sqft', models.IntegerField()),
                ('type_of_property', models.CharField(choices=[('Single Family', 'Single Family'), ('Condo', 'Condo'), ('Townhouse', 'Townhouse'), ('Multi-Family', 'Multi-Family'), ('Duplex', 'Duplex')], default='Single Family', max_length=50)),
                ('lot_size', models.DecimalField(decimal_places=1, max_digits=5)),
                ('pool', models.BooleanField(default=False)),
                ('heating', multiselectfield.db.fields.MultiSelectField(choices=[('Central', 'Central'), ('Electric', 'Electric'), ('Forced Air', 'Forced Air'), ('Natural Gas', 'Natural Gas'), ('Fireplace', 'Fireplace'), ('No data', 'No data')], default='None', max_length=70)),
                ('cooling', multiselectfield.db.fields.MultiSelectField(choices=[('Central', 'Central'), ('Electric', 'Electric'), ('No data', 'No data')], default='None', max_length=70)),
                ('year_built', models.IntegerField(default=2022)),
                ('photo_main', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('publishedAt', models.CharField(blank=True, max_length=100, null=True)),
                ('pub_date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 9, 4, 5, 43, 11, 229769))),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='realtor', to='realtors.realtor')),
            ],
            options={
                'ordering': ('-pub_date',),
                'unique_together': {('realtor', 'pub_date')},
            },
        ),
    ]
