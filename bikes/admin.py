
from django.contrib import admin
from .models import Bike
from django.utils.html import format_html


class BikeAdmin(admin.ModelAdmin):

    def thumbnail(self, object):
        return format_html(f'<img src="{object.bike_photo.url}" width="40" style="border-radius: 50px;" />')

    thumbnail.short_description = 'Bike Image'
    list_display = (
        'id', 'thumbnail', 'bike_title', 'city', 'color', 'model', 'year', 'body_style', 'fuel_type', 'price', 'is_featured')
    list_display_links = ('id', 'thumbnail', 'bike_title')
    list_editable = ('is_featured',)
    search_fields = ('id', 'bike_title', 'city', 'model', 'body_style', 'fuel_type')
    list_filter = ('city', 'model', 'body_style', 'fuel_type')


admin.site.register(Bike, BikeAdmin)
