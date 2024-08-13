from django.contrib import admin
from .models import Plot


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "area", "price", "image"]
    search_fields = ["name", "location"]
    list_filter = ["location"]
