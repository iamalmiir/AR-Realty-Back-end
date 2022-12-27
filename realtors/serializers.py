from rest_framework import serializers

from realtors.models import Realtor


class RealtorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Realtor
        fields = ["slug", "full_name", "photo", "description", "phone", "email", "is_mvp"]
