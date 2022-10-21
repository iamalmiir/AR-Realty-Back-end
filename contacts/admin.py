from django.contrib import admin

from contacts.models import Inquiry, BusinessInquiry


@admin.register(Inquiry)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("listing", "name", "email", "phone")
    list_display_links = (
        "listing",
        "name",
        "email",
        "phone",
    )
    search_fields = ("listing", "name", "email", "phone", "message", "user_id")
    list_per_page = 25


@admin.register(BusinessInquiry)
class BusinessContactAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "company_name", "phone")
    list_display_links = (
        "first_name",
        "last_name",
        "email",
        "company_name",
        "phone",
    )
    search_fields = (
        "first_name",
        "last_name",
        "email",
        "company_name",
        "phone",
    )
    list_per_page = 25


@admin.action(description="Delete all inquiries")
def delete_all_inquiries(modeladmin, request, queryset):
    queryset.delete()

    modeladmin.message_user(request, "All inquiries have been deleted")

    return None
