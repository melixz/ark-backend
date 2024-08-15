from django.contrib import admin
from .models import PlotBuilding


@admin.register(PlotBuilding)
class PlotBuildingAdmin(admin.ModelAdmin):
    list_display = ["name", "bgr_image", "path", "class_name"]
    search_fields = ["name", "path"]
    list_filter = ["class_name"]
