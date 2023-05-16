from django.contrib import admin
from .models import Item

# Register your models here.
class PropertyAdmin(admin.ModelAdmin):
    list_display = ("property", "status")
    list_filter = ("status",)
    search_fields = ("property", "description")

admin.site.register(Item, PropertyAdmin)
