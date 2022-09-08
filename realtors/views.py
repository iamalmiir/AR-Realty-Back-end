from rest_framework import generics
from rest_framework import permissions

from realtors.models import Realtor
from realtors.serializers import RealtorSerializer


class RealtorList(generics.ListCreateAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = (permissions.IsAdminUser,)


# Get the Realtor object by ID
class RealtorDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = RealtorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        # if not found DRF will raise a 404 error
        return Realtor.objects.filter(slug=slug)
