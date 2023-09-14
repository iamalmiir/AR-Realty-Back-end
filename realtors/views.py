from rest_framework.exceptions import NotFound
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from listings.models import Listing
from listings.serializers import ListingSerializer
from realtors.models import Realtor
from realtors.serializers import RealtorSerializer


class RealtorList(generics.ListCreateAPIView):
    # Set the default queryset to fetch all Realtor objects
    queryset = Realtor.objects.all()

    # Use the RealtorSerializer to serialize the Realtor data
    serializer_class = RealtorSerializer

    # Define permissions: If authenticated, users can list and create Realtors;
    # if not authenticated, they can only list.
    permission_classes = (AllowAny,)

    # @method_decorator(
    #     cache_page(60 * 60 * 24)
    # )  # Cache the results of this view for 24 hours
    def dispatch(self, *args, **kwargs):
        # Override the dispatch method to integrate caching behavior
        return super().dispatch(*args, **kwargs)


class RealtorDetail(generics.RetrieveAPIView):
    # Define the lookup field as 'slug' for fetching the Realtor object
    lookup_field = "slug"

    # Use the RealtorSerializer to serialize the data
    serializer_class = RealtorSerializer

    # Set permissions: If authenticated, the user can retrieve and modify;
    #  if not, only retrieve
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        # Fetch the 'slug' from the URL parameters
        slug = self.kwargs.get("slug")

        # Check if a Realtor object with the provided slug exists
        if not Realtor.objects.filter(slug=slug).exists():
            # If not, raise a NotFound exception with a custom error message
            raise NotFound({"error": "No Realtor found."})

        # Return the Realtor object(s) with the provided slug
        return Realtor.objects.filter(slug=slug)

    @method_decorator(
        cache_page(60 * 60 * 24)
    )  # Cache the result of this view for 24 hours
    def dispatch(self, *args, **kwargs):
        # Override the dispatch method to integrate caching
        return super().dispatch(*args, **kwargs)


class RealtorListings(generics.ListAPIView):
    # Define the lookup field as 'slug' to fetch listings
    # for a specific Realtor
    lookup_field = "slug"

    # Use the ListingSerializer to serialize the listing data
    serializer_class = ListingSerializer

    # Set permissions: If authenticated, users can retrieve and create
    # listings; if not, they can only retrieve
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        # Fetch the 'slug' from the URL parameters
        slug = self.kwargs.get("slug")

        # Check if a Realtor with the given slug exists
        if not Realtor.objects.filter(slug=slug).exists():
            # If no Realtor matches the provided slug, raise a NotFound
            # exception with a custom error message
            raise NotFound({"error": "Wrong Realtor. Try again."})

        # Return listings associated with the Realtor matching
        # the provided slug
        return Listing.objects.filter(realtor__slug=slug)

    @method_decorator(
        cache_page(60 * 60 * 2)
    )  # Cache the result of this view for 2 hours
    @method_decorator(
        vary_on_headers("slug")
    )  # Cache should vary based on the 'slug' header
    def dispatch(self, *args, **kwargs):
        # Override the dispatch method to integrate caching and vary caching
        # behavior on headers
        return super().dispatch(*args, **kwargs)
