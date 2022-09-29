from django.contrib import admin

from listings.models import Listing


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ["realtor", "title", "address", "state", "is_published"]
    list_filter = ["realtor", "is_published"]
    search_fields = ["title", "description"]
    list_per_page = 25
