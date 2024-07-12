from django.contrib import admin
from .models import Header, MainSection, FooterSection


class HeaderAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'logo', 'navigation_background_color', 'telegram_icon',
        'whatsapp_icon', 'viber_icon', 'phone_icon', 'header_background',
        'title', 'description'
    ]
    search_fields = ['title', 'description']


class MainSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['title']


class FooterSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content']
    search_fields = ['title']


admin.site.register(Header, HeaderAdmin)
admin.site.register(MainSection, MainSectionAdmin)
admin.site.register(FooterSection, FooterSectionAdmin)
