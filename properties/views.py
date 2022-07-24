from rest_framework import generics
from rest_framework import permissions

from properties.choices import get_state_abbreviation
from properties.models import Listing
from properties.pagination import SixResultsPagination
from properties.serializers import ListingSerializer


class ListingList(generics.ListCreateAPIView):
    queryset = Listing.objects.filter(is_published=True)

    serializer_class = ListingSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    pagination_class = SixResultsPagination


# Get the Property object by filtering by slug
class ListingDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = ListingSerializer

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        return Listing.objects.filter(slug=slug)


# Get listing based on search query
class SearchQuery(generics.ListAPIView):
    serializer_class = ListingSerializer

    def get_queryset(self):
        q = self.request.query_params.get("q")

        return (
                Listing.objects.filter(address__icontains=q)
                or Listing.objects.filter(city__icontains=q)
                or Listing.objects.filter(state__icontains=get_state_abbreviation(q))
                or Listing.objects.filter(zipcode__icontains=q)
                or Listing.objects.filter(title__icontains=q)
        )
