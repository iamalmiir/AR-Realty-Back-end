from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from contacts import views

urlpatterns = [
    path("contact/business-inquiries/", views.CreateBusinessInquiry.as_view()),
    path("inquiries/", views.CreateInquiry.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
