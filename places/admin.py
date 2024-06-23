from adminsortable2.admin import SortableAdminBase, SortableTabularInline
from django.contrib import admin
from django.db.models.functions import Concat
from django.utils.html import format_html

from .models import Place, PlaceCoordinate, PlaceImage


class ImagePreviewMixin:
    readonly_fields = ('preview',)

    def preview(self, instance):
        preview_height = instance.image.height if instance.image.height < 200 else 200
        return format_html(
            '<img src="{}" alt="preview" style="max-height: {}px">',
            instance.image.url,
            preview_height
        )


class PlaceImageInline(ImagePreviewMixin, SortableTabularInline):
    model = PlaceImage
    fields = ('number', 'image', 'preview')
    extra = 1
    ordering = ('number',)


class PlaceCoordinateInline(admin.StackedInline):
    model = PlaceCoordinate


@admin.register(Place)
class PlaceAdmin(SortableAdminBase, admin.ModelAdmin):
    list_display = ("id", "title")
    ordering = ('title',)
    prepopulated_fields = {'placeId': ('title',)}
    inlines = [PlaceCoordinateInline, PlaceImageInline]

    def get_list_display_links(self, request, list_display):
        return list_display


@admin.register(PlaceImage)
class PlaceImageAdmin(ImagePreviewMixin, admin.ModelAdmin):
    list_display = ('title', )
    ordering = ('place__title', 'number')

    def preview(self, instance):
        preview_height = instance.image.height if instance.image.height < 200 else 200
        return format_html(
            '<img src="{}" alt="preview" style="max-height: {}px">',
            instance.image.url,
            preview_height
        )

    @admin.display(description='локация', ordering=Concat('place__title', 'number'))
    def title(self, obj):
        return f'{obj.number} {obj.place.title}'

    def get_list_display_links(self, request, list_display):
        return list_display
