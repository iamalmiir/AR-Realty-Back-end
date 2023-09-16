from django.contrib import admin
from django.urls import path, include
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("jet/", include("jet.urls", "jet")),  # Django JET URLS
    path("api/", include("realtors.urls")),
    path("api/", include("listings.urls")),
    path("api/", include("contacts.urls")),
    path("api/user/", include("users.urls")),
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("admin/", admin.site.urls),
    path("docs/", include_docs_urls(title="AR Realty")),
    path(
        "openapi",
        get_schema_view(
            title="AR Realty", description="API AR Realty Front end", version="1.0.0"
        ),
        name="openapi-schema",
    ),
]
