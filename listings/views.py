from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from rest_framework import generics
from rest_framework import permissions

from listings.choices import get_state_abbreviation
from listings.models import Listing
from listings.pagination import SixResultsPagination
from listings.serializers import ListingSerializer


class ListingList(generics.ListAPIView):
    queryset = Listing.objects.filter(is_published=True)

    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = SixResultsPagination

    @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# Get the Property object by slug
class ListingDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Listing.objects.filter(slug=slug)

    @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# Get listing based on search query
class SearchQuery(generics.ListAPIView):
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        q = self.request.query_params.get("q")

        return (
                Listing.objects.filter(address__icontains=q)
                or Listing.objects.filter(city__icontains=q)
                or Listing.objects.filter(state__icontains=get_state_abbreviation(q))
                or Listing.objects.filter(zipcode__icontains=q)
                or Listing.objects.filter(title__icontains=q)
        )


class RealtorListings(generics.ListCreateAPIView):
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        realtor = self.request.headers.get("Realtor")
        return Listing.objects.filter(realtor__slug=realtor)

    @method_decorator(cache_page(60 * 60 * 24))
    @method_decorator(vary_on_headers('Realtor'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# Return 3 random listings excluding the current listing
class RandomListings(generics.ListAPIView):
    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        slug = self.request.query_params.get("slug")
        return Listing.objects.filter(is_published=True).exclude(slug=slug).order_by("?")[:3]

    @method_decorator(cache_page(60 * 60 * 24))
    @method_decorator(vary_on_headers('slug'))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
