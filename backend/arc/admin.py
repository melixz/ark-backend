from django.contrib import admin
from .models import City, Complex, Section


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


class ComplexInline(admin.TabularInline):
    model = Complex
    extra = 1


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name', 'path')
    search_fields = ('name',)
    inlines = [ComplexInline]


@admin.register(Complex)
class ComplexAdmin(admin.ModelAdmin):
    list_display = ('name', 'city')
    search_fields = ('name', 'city__name')
    inlines = [SectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'complex')
    search_fields = ('title', 'complex__name')
