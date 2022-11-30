import datetime
from uuid import uuid4

import cloudinary.uploader
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse


class Realtor(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    full_name = models.CharField(max_length=100)
    slug = models.SlugField(editable=False, unique=True, max_length=50, null=True, blank=True)
    photo = models.ImageField(upload_to="realtors/%Y/%m/%d/", on_delete=cloudinary.uploader.destroy, blank=True)
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateTimeField(default=datetime.datetime.now, blank=True)

    class Meta:
        ordering = ("-hire_date",)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse("full_name", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        value = self.full_name + "-" + str(self.email[:5])
        self.slug = slugify(
            value,
        )
        super().save(*args, **kwargs)
