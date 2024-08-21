from django.contrib import admin
from .models import Developer


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ["title", "path"]
    search_fields = ["title", "path"]
