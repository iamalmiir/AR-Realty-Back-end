from datetime import datetime
from uuid import uuid4

from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from multiselectfield import MultiSelectField

from listings.choices import COOLING_CHOICES, HEATING_CHOICES, US_STATES, LISTING_TYPES
from realtors.models import Realtor

LISTING_PHOTOS = "ar/listings/"


class Listing(models.Model):
    id = models.UUIDField(
        primary_key=True,
        unique=True,
        default=uuid4,
        editable=False,
    )

    slug = models.SlugField(editable=False, unique=True, max_length=50, null=True, blank=True)
    title = models.CharField(max_length=70)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2, choices=US_STATES)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    type_of_property = models.CharField(
        max_length=50, choices=LISTING_TYPES, default="Single Family"
    )
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    pool = models.BooleanField(default=False)
    heating = MultiSelectField(max_length=70, choices=HEATING_CHOICES, default="None")
    cooling = MultiSelectField(max_length=70, choices=COOLING_CHOICES, default="None")
    year_built = models.IntegerField(default=datetime.now().year)

    # Media fields with cloudinary plus optimization are implemented
    photo_main = models.ImageField(upload_to=LISTING_PHOTOS, blank=False)
    photo_1 = models.ImageField(upload_to=LISTING_PHOTOS, blank=True)
    photo_2 = models.ImageField(upload_to=LISTING_PHOTOS, blank=True)
    photo_3 = models.ImageField(upload_to=LISTING_PHOTOS, blank=True)
    photo_4 = models.ImageField(upload_to=LISTING_PHOTOS, blank=True)
    photo_5 = models.ImageField(upload_to=LISTING_PHOTOS, blank=True)

    is_published = models.BooleanField(default=True)
    publishedAt = models.DateField(default=datetime.now, null=False)
    realtor = models.ForeignKey(Realtor, related_name="realtor", on_delete=models.DO_NOTHING)

    class Meta:
        ordering = ("-publishedAt",)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("title", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        value = self.title + "-" + str(self.realtor.full_name)
        self.slug = slugify(
            value,
        )
        super().save(*args, **kwargs)
