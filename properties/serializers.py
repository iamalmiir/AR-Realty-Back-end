from unicodedata import lookup
from rest_framework import serializers

from properties.models import Listing
from realtors.serializers import RealtorSerializer


class ListingSerializer(serializers.ModelSerializer):
    realtor = RealtorSerializer()

    class Meta:
        model = Listing
        fields = "__all__"
