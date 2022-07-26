from rest_framework import serializers

from realtors.models import Realtor


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = ["full_name", "photo", "description", "phone", "email"]
