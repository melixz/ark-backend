from django.contrib import admin
from .models import (
    Header,
    MainContent,
    SectionOne,
    SectionTwo,
    SectionTwoCard,
    SectionThree,
    Footer,
)
from .forms import MainContentForm


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


class MainContentAdmin(admin.ModelAdmin):
    form = MainContentForm
    list_display = ["name", "bgr_image", "path"]
    search_fields = ["name"]
    list_filter = ["name"]


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


class SectionTwoCardAdmin(admin.ModelAdmin):
    list_display = ["icon", "title", "description", "background", "button_text"]
    search_fields = ["title", "description"]
    list_filter = ["title"]


class SectionTwoAdmin(admin.ModelAdmin):
    list_display = ["title"]
    search_fields = ["title"]
    filter_horizontal = ["cards"]


class SectionThreeAdmin(admin.ModelAdmin):
    list_display = ["image", "tg_link", "viber_link", "whatsup_link", "bgr_button"]
    search_fields = ["tg_link", "viber_link", "whatsup_link"]
    list_filter = ["tg_link"]


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


admin.site.register(Header, HeaderAdmin)
admin.site.register(MainContent, MainContentAdmin)
admin.site.register(SectionOne, SectionOneAdmin)
admin.site.register(SectionTwoCard, SectionTwoCardAdmin)
admin.site.register(SectionTwo, SectionTwoAdmin)
admin.site.register(SectionThree, SectionThreeAdmin)
admin.site.register(Footer, FooterAdmin)
