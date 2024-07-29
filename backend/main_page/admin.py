from django.contrib import admin
from .models import Header, MainSection, Footer, Content


class HeaderAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "logo",
        "navigation_background_color",
        "phone_icon",
        "header_background",
        "title",
        "description",
    ]
    search_fields = ["title", "description"]
    list_filter = ["navigation_background_color"]


class ContentInline(admin.TabularInline):
    model = Content
    extra = 1


class MainSectionAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "image", "url", "content_list"]
    search_fields = ["title"]
    list_filter = ["title"]
    inlines = [ContentInline]

    def content_list(self, obj):
        return ", ".join([content.content for content in obj.contents.all()])

    content_list.short_description = "Content List"


class FooterAdmin(admin.ModelAdmin):
    list_display = ["id", "telegram_icon", "whatsapp_icon", "viber_icon", "vk_icon"]
    search_fields = ["telegram_icon", "whatsapp_icon", "viber_icon", "vk_icon"]
    list_filter = ["telegram_icon", "whatsapp_icon", "viber_icon", "vk_icon"]


admin.site.register(Header, HeaderAdmin)
admin.site.register(MainSection, MainSectionAdmin)
admin.site.register(Footer, FooterAdmin)
