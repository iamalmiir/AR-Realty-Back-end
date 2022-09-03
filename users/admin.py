from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import TextInput, Textarea

from users.models import User


class UserAdminConfig(UserAdmin):
    # Display options for the admin site are defined here.
    list_display = (
        "email",
        "username",
        "full_name",
        "is_staff",
        "is_superuser",
        "is_active",
    )
    # The fields to display in the admin site are defined here.
    list_filter = ("email", "is_staff", "is_superuser", "is_active")
    # The fields to search in the admin site are defined here.
    search_fields = ("email", "username", "full_name")
    # Ordering options for the admin site are defined here.
    ordering = ("-start_date",)
    fieldsets = (
        (None, {"fields": ("avatar", "email", "password")}),
        (
            "Personal info",
            {"fields": ("username", "full_name", "start_date")},
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
    )
    formfield_overrides = {
        models.CharField: {"widget": TextInput(attrs={"size": "20"})},
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }


admin.site.register(User, UserAdminConfig)
