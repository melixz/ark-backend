from django.contrib import admin
from .models import City, Complex, Plot, Section, Apartment, ApartmentImage


class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1


class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1


class ComplexInline(admin.TabularInline):
    model = Complex
    extra = 1
    inlines = [ApartmentInline]


class PlotInline(admin.TabularInline):
    model = Plot
    extra = 1


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "path", "card_bg", "bg")
    search_fields = ("name",)
    fieldsets = (
        (None, {
            'fields': ('name', 'path', 'card_bg', 'bg', 'new_title', 'new_desc', 'plot_title', 'plot_desc')
        }),
    )
    inlines = [ComplexInline, PlotInline, SectionInline]


@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "bg")
    search_fields = ("name", "city__name")
    inlines = [ApartmentInline]


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("category", "complex")
    search_fields = ("category", "complex__name")
    inlines = [ApartmentImageInline]


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ("district", "city", "path", "card_bg", "bg")
    search_fields = ("district", "city__name")


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "city", "loc")
    search_fields = ("title", "city__name", "loc")
