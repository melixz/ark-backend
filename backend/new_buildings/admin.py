from django.contrib import admin
from .models import NewBuilding
from .forms import NewBuildingForm


class NewBuildingAdmin(admin.ModelAdmin):
    form = NewBuildingForm
    list_display = ["name", "bgr_image", "path", "class_name"]
    search_fields = ["name", "path"]
    list_filter = ["class_name"]


admin.site.register(NewBuilding, NewBuildingAdmin)
