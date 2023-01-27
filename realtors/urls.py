from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from realtors import views

urlpatterns = [
    path("realtors/", views.RealtorList.as_view()),
    path("realtor/info/<slug:slug>/", views.RealtorDetail.as_view()),
    path("realtor/listings/<slug:slug>/", views.RealtorListings.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
