from django.contrib import admin
from .models import Header, MainContent, SectionOne, Card, Footer
from .forms import CardForm


@admin.register(Header)
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
    list_filter = ["header_title"]


@admin.register(MainContent)
class MainContentAdmin(admin.ModelAdmin):
    list_display = ["name", "bgr_image", "path", "class_name"]
    search_fields = ["name"]
    list_filter = ["name"]


@admin.register(SectionOne)
class SectionOneAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "desc",
        "climate",
        "nature",
        "accessibility",
        "infrastructure",
        "possibilities",
    ]
    search_fields = ["title", "desc"]
    list_filter = ["title"]


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    form = CardForm
    list_display = ["title", "description", "path", "image"]
    search_fields = ["title", "description"]
    list_filter = ["title"]


@admin.register(Footer)
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
    list_filter = ["phone_number"]
