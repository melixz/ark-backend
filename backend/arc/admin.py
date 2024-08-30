from django.contrib import admin
from .models import City, Complex, Plot, Section


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


class ComplexInline(admin.TabularInline):
    model = Complex
    extra = 1


class PlotInline(admin.TabularInline):
    model = Plot
    extra = 1


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'path')
    search_fields = ('name',)
    inlines = [ComplexInline, PlotInline, SectionInline]


@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city__name')


@admin.register(Plot)
class PlotAdmin(admin.ModelAdmin):
    list_display = ('district', 'city', 'path')
    search_fields = ('district', 'city__name')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'loc')
    search_fields = ('title', 'city__name', 'loc')
