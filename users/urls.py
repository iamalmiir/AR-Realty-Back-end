from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from users import views

urlpatterns = [
    path("me/", views.UserView.as_view(), name="user"),
    # path("<uuid:id>/", views.UpdateDeleteUserViewSet.as_view(), name="user"),
    path("register/", views.RegisterUser.as_view(), name="register"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
