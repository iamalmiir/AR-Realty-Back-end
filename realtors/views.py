from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from realtors.models import Realtor
from realtors.serializers import RealtorSerializer


class RealtorList(generics.ListCreateAPIView):
    queryset = Realtor.objects.all()
    serializer_class = RealtorSerializer
    permission_classes = (AllowAny,)

    @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


# Get the Realtor object by ID
class RealtorDetail(generics.RetrieveAPIView):
    lookup_field = "slug"
    serializer_class = RealtorSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        slug = self.kwargs.get("slug")
        # if not found DRF will raise a 404 error
        return Realtor.objects.filter(slug=slug)

    @method_decorator(cache_page(60 * 60 * 24))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
