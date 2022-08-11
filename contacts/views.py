from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

from contacts.models import Inquiry, BusinessInquiry
from contacts.serializers import InquirySerializer, BusinessInquirySerializer
from properties.models import Listing


# Create InquiryViewSet
class CreateInquiry(ListCreateAPIView):
    serializer_class = InquirySerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        user, inquiry = self.request.user, self.request.data
        print(self.request.data)
        inquiry["user_id"] = user.id
        inquiry["name"] = user.full_name
        inquiry["email"] = user.email

        inquiry_exists = Inquiry.objects.filter(listing_id=inquiry["listing_id"], user_id=user.id).exists()
        listing_exists = Listing.objects.filter(id=inquiry["listing_id"]).exists()
        if not inquiry_exists and listing_exists:
            serializer.save(**inquiry)
        else:
            raise ValueError("User already has an inquiry for this listing or listing does not exist")

    def get_queryset(self):
        user_id = self.request.user.id
        return Inquiry.objects.filter(user_id=user_id)


class CreateBusinessInquiry(ListCreateAPIView):
    serializer_class = BusinessInquirySerializer
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        email, company = self.request.data["email"], self.request.data["company_name"]
        inquiry_exists = BusinessInquiry.objects.filter(email=email, company_name=company).exists()

        if inquiry_exists:
            raise ValueError("User already has an inquiry")
        else:
            serializer.save(**self.request.data)

    def get_queryset(self):
        user_id = self.request.user.id
        return BusinessInquiry.objects.filter(user_id=user_id)
