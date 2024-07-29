from django.contrib import admin
from .models import (
    Header,
    MainContent,
    Section1,
    Section2,
    Section2Card,
    Section3,
    Footer,
)


class HeaderAdmin(admin.ModelAdmin):
    list_display = [
        "logo_icon",
        "phone_icon",
        "phone_number",
        "header_bgr",
        "header_title",
        "header_title_bottom",
        "nav_bgr",
        "bgr_bottom",
    ]
    search_fields = ["header_title", "header_title_bottom"]


class MainContentAdmin(admin.ModelAdmin):
    list_display = ["name", "bgr_image", "url"]
    search_fields = ["name"]


class Section1Admin(admin.ModelAdmin):
    list_display = [
        "title",
        "desc",
        "climate",
        "nature",
        "assessability",
        "infrastructure",
        "possibilities",
    ]
    search_fields = ["title", "desc"]


class Section2CardAdmin(admin.ModelAdmin):
    list_display = ["icon", "title", "description", "background", "button_text"]
    search_fields = ["title", "description"]


class Section2Admin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    filter_horizontal = ["cards"]


class Section3Admin(admin.ModelAdmin):
    list_display = ["image", "tg_link", "viber_link", "whatsup_link", "bgr_button"]
    search_fields = ["tg_link", "viber_link", "whatsup_link"]


class FooterAdmin(admin.ModelAdmin):
    list_display = [
        "telegram_icon",
        "whatsapp_icon",
        "viber_icon",
        "youtube_icon",
        "vk_icon",
        "phone_number",
        "color_text",
    ]
    search_fields = ["phone_number"]


admin.site.register(Header, HeaderAdmin)
admin.site.register(MainContent, MainContentAdmin)
admin.site.register(Section1, Section1Admin)
admin.site.register(Section2Card, Section2CardAdmin)
admin.site.register(Section2, Section2Admin)
admin.site.register(Section3, Section3Admin)
admin.site.register(Footer, FooterAdmin)
