from django.contrib import admin
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
    NewSection,
    PlotSection,
)


class ComplexImageInline(admin.TabularInline):
    model = ComplexImage
    extra = 1


class PlotImageInline(admin.TabularInline):
    model = PlotImage
    extra = 1


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1


class ApartmentSectionInline(admin.StackedInline):
    model = ApartmentSection
    extra = 1


class PlotLandInline(admin.TabularInline):
    model = PlotLand
    extra = 1


class NewSectionInline(admin.StackedInline):
    model = NewSection
    extra = 1


class PlotSectionInline(admin.StackedInline):
    model = PlotSection
    extra = 1


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "path",
        "complex_card_bg",
        "complex_bg",
        "plot_card_bg",
        "plot_bg",
    )
    search_fields = ("name",)
    inlines = [NewSectionInline, PlotSectionInline]


@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "path", "card_bg")
    search_fields = ("name", "city__name")
    inlines = [ComplexImageInline]


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("category", "complex", "city")
    search_fields = ("complex__name", "city__name")
    inlines = [ApartmentImageInline, ApartmentSectionInline]


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ("district", "city", "path", "card_bg")
    search_fields = ("district", "city__name")
    inlines = [PlotImageInline, PlotLandInline]


@admin.register(PlotLand)
class PlotLandAdmin(admin.ModelAdmin):
    list_display = ("plot", "land_type", "price")
    search_fields = ("plot__district", "land_type")


@admin.register(NewSection)
class NewSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "loc")
    search_fields = ("title", "city__name", "loc")


@admin.register(PlotSection)
class PlotSectionAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "loc")
    search_fields = ("title", "city__name", "loc")
