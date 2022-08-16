from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.models import Inquiry
from properties.models import Listing
from properties.serializers import ListingSerializer
from users.serializers import RegisterUserSerializer


class RegisterView(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Nice! You are now registered."}, status=status.HTTP_201_CREATED)

        if serializer.errors.get('user_name', None) or serializer.errors.get('email', None):
            return Response({"message": "User name or email is already taken"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"message": "Something went wrong. Please try again."}, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        remove_data = ["password", "_state", "is_superuser", "is_staff", "is_active", "date_joined", "last_login",
                       "start_date"]
        user_data = request.user.__dict__
        user = {key: user_data[key] for key in user_data if key not in remove_data}
        return Response(user, status=status.HTTP_200_OK)


class UserDashboard(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        user_contacts = Inquiry.objects.order_by("-contact_date").filter(user_id=request.user.id)
        user_listings = Listing.objects.filter(id__in=[listing.listing_id for listing in user_contacts])
        user_listings_data = ListingSerializer(user_listings, many=True)

        return Response(user_listings_data.data)
