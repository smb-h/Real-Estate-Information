from django.contrib import admin
from app.models import Property


@admin.register(Property)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (("Property", {"fields": ("area", "sector", "url")}),)
    list_display = ["id", "url"]
    search_fields = ["id", "url", "area", "sector"]

