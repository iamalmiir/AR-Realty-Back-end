from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    path("register/", views.RegisterUser.as_view(), name="register"),
    path("me/", views.UserView.as_view(), name="user"),
    path("dashboard/", views.UserDashboard.as_view(), name="dashboard"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
