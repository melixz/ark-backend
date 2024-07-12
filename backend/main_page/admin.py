from django.contrib import admin
from .models import Header, MainSection, FooterSection


class HeaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'left_image', 'left_alt', 'center_text']
    search_fields = ['left_alt', 'center_text']


class MainSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['title']


class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['title']


admin.site.register(Header, HeaderAdmin)
admin.site.register(MainSection, MainSectionAdmin)
admin.site.register(FooterSection, FooterSectionAdmin)
