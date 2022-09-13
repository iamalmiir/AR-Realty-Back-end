from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics

from contacts.models import Inquiry
from properties.models import Listing
from users.models import User
from properties.serializers import ListingSerializer
from users.serializers import RegisterUserSerializer
from users.helpers.profanity_filters import profanity_filter


class RegisterUser(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)

    @staticmethod
    def post(request):
        try:
            profanity_filter(request.data)
            serializer = RegisterUserSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Nice! You are now registered."}, status=status.HTTP_201_CREATED
                )

            if serializer.errors.get("username", None) or serializer.errors.get("email", None):
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


class UserView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get(request):
        # get reqest headers
        dashboard_data = request.headers.get("Dashboard", None)
        if dashboard_data == "true":
            user_contacts = Inquiry.objects.order_by("-contact_date").filter(
                user_id=request.user.id
            )
            user_listings = Listing.objects.filter(
                id__in=[listing.listing_id for listing in user_contacts]
            )
            user_listings_data = ListingSerializer(user_listings, many=True)

            return Response(user_listings_data.data)

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
        user_data = request.user.__dict__
        user = {key: user_data[key] for key in user_data if key not in remove_data}
        return Response(user, status=status.HTTP_200_OK)

    @staticmethod
    def put(request):
        try:
            user = User.objects.get(id=request.user.id)
            if user.id != request.user.id:
                return Response(
                    {"message": "You are not authorized to view this user."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            serializer = RegisterUserSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                # change password, if provided in request
                if request.data.get("password", None):
                    user.set_password(request.data["password"])

                # if user is updating their email, check if email is already taken
                if request.data.get("email", None):
                    if User.objects.filter(email=request.data["email"]).exists():
                        return Response(
                            {"message": "Email is already taken."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    user.email = request.data["email"]

                # if user is updating their username, check if username is already taken
                if request.data.get("username", None):
                    if User.objects.filter(username=request.data["username"]).exists():
                        return Response(
                            {"message": "Username is already taken."},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                    user.username = request.data["username"]

                # if user is updating their full name, check if profanity is in full name
                if request.data.get("full_name", None):
                    profanity_filter(request.data)
                    user.full_name = request.data["full_name"]

                serializer.save()
                return Response({"message": "User updated successfully"}, status=status.HTTP_200_OK)
            return Response(
                {"message": "Something went wrong. Please try again."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)

    def delete(request):
        try:
            user = User.objects.get(id=request.user.id)
            if user.id != request.user.id:
                return Response(
                    {"message": "You are not authorized to view this user."},
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"message": "User does not exist"}, status=status.HTTP_404_NOT_FOUND)
