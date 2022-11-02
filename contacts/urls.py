from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from contacts import views

urlpatterns = [
    path("inquiries/", views.CreateInquiry.as_view()),
    path("contact/business-inquiries/", views.CreateBusinessInquiry.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
