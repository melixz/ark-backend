from django.contrib import admin
from .models import Plot


class PlotAdmin(admin.ModelAdmin):
    list_display = ["name", "location", "area", "price", "image"]
    search_fields = ["name", "location"]
    list_filter = ["location"]


admin.site.register(Plot)
