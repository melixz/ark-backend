from django.contrib import admin
from .models import City, Complex, Plot, Apartment, ApartmentImage, PlotLand, NewSection, PlotSection


# Inlines для квартир и комплексов
class ApartmentImageInline(admin.TabularInline):
    model = ApartmentImage
    extra = 1


class ApartmentInline(admin.TabularInline):
    model = Apartment
    extra = 1
    inlines = [ApartmentImageInline]


class ComplexInline(admin.StackedInline):
    model = Complex
    extra = 1
    inlines = [ApartmentInline]


# Inlines для участков и застроек
class PlotLandInline(admin.TabularInline):
    model = PlotLand
    extra = 1


class PlotInline(admin.StackedInline):
    model = Plot
    extra = 1
    inlines = [PlotLandInline]


# Inlines для секций новостроек и застроек
class NewSectionInline(admin.StackedInline):
    model = NewSection
    extra = 1


class PlotSectionInline(admin.StackedInline):
    model = PlotSection
    extra = 1


# Основная админка для города
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "path", "complex_card_bg", "complex_bg", "plot_card_bg", "plot_bg")
    search_fields = ("name",)
    fieldsets = (
        (None, {
            'fields': (
                'name', 'path', 'complex_card_bg', 'complex_bg', 'plot_card_bg', 'plot_bg',
                'new_title', 'new_desc', 'plot_title', 'plot_desc'
            )
        }),
    )
    inlines = [ComplexInline, PlotInline, NewSectionInline, PlotSectionInline]


# Отдельные админки для других моделей (если нужно редактировать их отдельно)
@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "bg")
    search_fields = ("name", "city__name")
    inlines = [ApartmentInline]


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ("category", "complex", "city")
    search_fields = ("category", "complex__name")
    inlines = [ApartmentImageInline]

    def save_model(self, request, obj, form, change):
        if not obj.city:
            obj.city = obj.complex.city
        super().save_model(request, obj, form, change)


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ("district", "city", "path", "card_bg", "bg")
    search_fields = ("district", "city__name")
    inlines = [PlotLandInline]


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
