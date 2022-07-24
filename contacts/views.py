from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from contacts.models import Inquiry, BusinessInquiry
from contacts.serializers import InquirySerializer, BusinessInquirySerializer
from properties.models import Listing


# Create InquiryViewSet
class CreateInquiry(generics.ListCreateAPIView):
    serializer_class = InquirySerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user_id, inquiry = self.request.user.id, self.request.data
        inquiry["user_id"] = user_id
        listing_id = inquiry["listing_id"]

        listing_exists = Listing.objects.filter(id=listing_id).exists()
        inquiry_exists = Inquiry.objects.filter(listing_id=listing_id, user_id=user_id).exists()

        if listing_exists and not inquiry_exists:
            raise ValueError("User already has an inquiry for this listing")
        else:
            serializer.save(**inquiry)

    def get_queryset(self):
        user_id = self.request.user.id
        return Inquiry.objects.filter(user_id=user_id)


class CreateBusinessInquiry(generics.ListCreateAPIView):
    serializer_class = BusinessInquirySerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        email, company = self.request.data["email"], self.request.data["company_name"]
        if BusinessInquiry.objects.filter(email=email, company_name=company).exists():
            raise ValueError("User already has an inquiry")
        else:
            serializer.save(**self.request.data)

    def get_queryset(self):
        user_id = self.request.user.id
        return BusinessInquiry.objects.filter(user_id=user_id)
