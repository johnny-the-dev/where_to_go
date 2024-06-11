from django.contrib import admin
from django.db.models.functions import Concat

from .models import Place, PlaceCoordinate, PlaceImage


class PlaceImageInline(admin.TabularInline):
    model = PlaceImage
    extra = 1
    classes = ("collapse",)


class PlaceCoordinateInline(admin.StackedInline):
    model = PlaceCoordinate


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    ordering = ('title',)
    inlines = [PlaceImageInline, PlaceCoordinateInline]

    def get_list_display_links(self, request, list_display):
        return list_display


@admin.register(PlaceImage)
class PlaceImageAdmin(admin.ModelAdmin):
    list_display = ('title', )
    ordering = ('place__title', 'number')

    @admin.display(description='локация', ordering=Concat('place__title', 'number'))
    def title(self, obj):
        return f'{obj.number} {obj.place.title}'

    def get_list_display_links(self, request, list_display):
        return list_display
