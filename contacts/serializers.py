from rest_framework import serializers

from contacts.models import Inquiry, BusinessInquiry
from realtors.serializers import RealtorSerializer


class InquirySerializer(serializers.ModelSerializer):
    realtor = RealtorSerializer(read_only=True)

    class Meta:
        model = Inquiry
        fields = "__all__"


class BusinessInquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessInquiry
        fields = "__all__"
