from django.contrib import admin
from django.utils.html import format_html
from .models import (
    City,
    Complex,
    Plot,
    ComplexImage,
    PlotImage,
    Apartment,
    ApartmentImage,
    ApartmentSection,
    PlotLand,
    PlotLandImage,
    NewSection,
    PlotSection,
    PlotLandSection,
    DynamicFormSubmission,
)


# Инлайны для изображений и секций
class ComplexImageInline(admin.TabularInline):
    model = ComplexImage
    extra = 1


class PlotImageInline(admin.TabularInline):
    model = PlotImage
    extra = 1


class PlotLandImageInline(admin.TabularInline):
    model = PlotLandImage
    extra = 1


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1


class ApartmentSectionInline(admin.StackedInline):
    model = ApartmentSection
    extra = 1
    fields = (
        "title",
        "price",
        "floor",
        "room_count",
        "apartment_number",
        "area",
        "delivery_date",
    )
    readonly_fields = ("apartment_number",)


class PlotLandSectionInline(admin.StackedInline):
    model = PlotLandSection
    extra = 1
    fields = (
        "title",
        "price",
        "area",
        "land_status",
        "gas",
        "electricity",
        "water",
        "sewage",
    )


class NewSectionInline(admin.StackedInline):
    model = NewSection
    extra = 1


class PlotSectionInline(admin.StackedInline):
    model = PlotSection
    extra = 1


# Администратор для города
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "path",
        "complex_card_bg_thumbnail",
        "complex_bg_thumbnail",
        "plot_card_bg_thumbnail",
        "plot_bg_thumbnail",
    )
    search_fields = ("name",)
    inlines = [NewSectionInline, PlotSectionInline]
    list_filter = ("name",)
    readonly_fields = ("path",)

    def complex_card_bg_thumbnail(self, obj):
        if obj.complex_card_bg:
            return format_html(
                '<img src="{}" style="height: 50px;"/>', obj.complex_card_bg.url
            )
        return "-"

    complex_card_bg_thumbnail.short_description = "Фон карточки (комплексы)"

    def complex_bg_thumbnail(self, obj):
        if obj.complex_bg:
            return format_html(
                '<img src="{}" style="height: 50px;"/>', obj.complex_bg.url
            )
        return "-"

    complex_bg_thumbnail.short_description = "Фон (комплексы)"

    def plot_card_bg_thumbnail(self, obj):
        if obj.plot_card_bg:
            return format_html(
                '<img src="{}" style="height: 50px;"/>', obj.plot_card_bg.url
            )
        return "-"

    plot_card_bg_thumbnail.short_description = "Фон карточки (застройки)"

    def plot_bg_thumbnail(self, obj):
        if obj.plot_bg:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.plot_bg.url)
        return "-"

    plot_bg_thumbnail.short_description = "Фон (застройки)"


# Администратор для комплекса
@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "path", "card_bg_thumbnail")
    search_fields = ("name", "city__name")
    list_filter = ("city",)
    inlines = [ComplexImageInline]
    readonly_fields = ("path",)
    autocomplete_fields = ["city"]
    list_select_related = ("city",)

    def card_bg_thumbnail(self, obj):
        if obj.card_bg:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.card_bg.url)
        return "-"

    card_bg_thumbnail.short_description = "Фон карточки"


# Администратор для квартиры
@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = (
        "category",
        "complex",
        "city",
        "path",
        "floor_count",
    )
    search_fields = ("complex__name", "city__name")
    inlines = [ApartmentImageInline, ApartmentSectionInline]
    readonly_fields = ("path",)
    list_filter = ("category", "complex", "city")
    autocomplete_fields = ["complex", "city"]
    list_select_related = ("complex", "city")


# Администратор для застройки
@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ("district", "city", "path", "card_bg_thumbnail")
    search_fields = ("district", "city__name")
    inlines = [PlotImageInline]
    readonly_fields = ("path",)
    list_filter = ("city",)
    autocomplete_fields = ["city"]
    list_select_related = ("city",)

    def card_bg_thumbnail(self, obj):
        if obj.card_bg:
            return format_html('<img src="{}" style="height: 50px;"/>', obj.card_bg.url)
        return "-"

    card_bg_thumbnail.short_description = "Фон карточки"


# Администратор для земельного участка
@admin.register(PlotLand)
class PlotLandAdmin(admin.ModelAdmin):
    list_display = ("plot", "land_type", "price", "path")
    search_fields = ("plot__district", "land_type")
    readonly_fields = ("path",)
    inlines = [PlotLandImageInline, PlotLandSectionInline]
    list_filter = ("land_type", "plot")
    autocomplete_fields = ["plot"]
    list_select_related = ("plot",)


# Администратор для секции новостроек
@admin.register(NewSection)
class NewSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "loc")
    search_fields = ("title", "city__name", "loc")
    list_filter = ("city",)
    autocomplete_fields = ["city"]
    list_select_related = ("city",)


# Администратор для секции застроек
@admin.register(PlotSection)
class PlotSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "loc")
    search_fields = ("title", "city__name", "loc")
    list_filter = ("city",)
    autocomplete_fields = ["city"]
    list_select_related = ("city",)


# Администратор для отправок форм
@admin.register(DynamicFormSubmission)
class DynamicFormSubmissionAdmin(admin.ModelAdmin):
    list_display = ("name", "submitted_at")
    readonly_fields = ("submitted_at", "data")
    search_fields = ("name",)
    list_filter = ("name", "submitted_at")
