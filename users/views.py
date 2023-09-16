from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from contacts.models import Inquiry
from listings.models import Listing
from listings.serializers import ListingSerializer
from users.helpers.profanity_filters import profanity_filter
from users.models import User
from users.serializers import RegisterUserSerializer


class RegisterUser(APIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        try:
            profanity_filter(request.data)
            serializer = RegisterUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Nice! You are now registered."},
                    status=status.HTTP_201_CREATED,
                )

            if serializer.errors.get("username", None) or serializer.errors.get(
                "email", None
            ):
                return Response(
                    {"message": "User name or email is already taken"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            return Response(
                {"message": "Something went wrong. Please try again."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except ValueError as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


"""
    UserView
    - GET: Get user data
    - PUT: Update user data
    - DELETE: Delete user data
"""


class UserView(APIView):
    permission_classes = (IsAuthenticated,)
    page_size = 6

    @staticmethod
    def get(request):
        dashboard_data = request.headers.get("Dashboard", None)
        if dashboard_data == "true":
            user_contacts = Inquiry.objects.order_by("-contact_date").filter(
                user=request.user.id
            )
            user_listings = Listing.objects.filter(
                id__in=[listing.listing for listing in user_contacts]
            )
            user_listings = ListingSerializer(user_listings, many=True).data
            return Response(user_listings, status=status.HTTP_200_OK)
        remove_data = [
            "password",
            "_state",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
            "last_login",
            "start_date",
        ]

        already_made_inquiry = request.headers.get("CheckInquiry", None)
        if already_made_inquiry == "check":
            listing_id = request.headers.get("ListingId", None)
            if listing_id:
                # Check if the user has already made an inquiry for this listing
                if Inquiry.objects.filter(
                    user=request.user.id, listing=listing_id
                ).exists():
                    return Response(
                        {"inquiry_made": "true"},
                        status=status.HTTP_200_OK,
                    )

        user_data = request.user.__dict__
        user = {key: user_data[key] for key in user_data if key not in remove_data}
        return Response(user, status=status.HTTP_200_OK)

    @staticmethod
    def put(request):
        # profanity_filter(request.data)
        user = User.objects.get(id=request.user.id)
        serializer = RegisterUserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User updated successfully"}, status=status.HTTP_200_OK
            )

        if serializer.errors.get("username", None) or serializer.errors.get(
            "email", None
        ):
            try:
                user = User.objects.get(id=request.user.id)
                profanity_filter(request.data)
                serializer = RegisterUserSerializer(
                    user, data=request.data, partial=True
                )
                if serializer.is_valid():
                    serializer.save()
                    return Response(
                        {"message": "User updated successfully."},
                        status=status.HTTP_200_OK,
                    )
                return Response(
                    {"message": "Something went wrong. Please try again."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except ValueError as e:
                return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @staticmethod
    def delete(request):
        try:
            user = User.objects.get(id=request.user.id)
            if user.id is not request.user.id:
                return Response(
                    {"message": "You are not authorized to view this user."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            user.delete()
            return Response(
                {"message": "User deleted successfully"}, status=status.HTTP_200_OK
            )
        except User.DoesNotExist:
            return Response(
                {"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND
            )
