from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from listings import views

urlpatterns = [
    path("listings/", views.ListingList.as_view()),
    path("listings/quicksearch/", views.SearchQuery.as_view()),
    path("listings/realtor/", views.RealtorListings.as_view()),
    path("listings/random/", views.RandomListings.as_view()),
    path("listings/<slug:slug>/", views.ListingDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
