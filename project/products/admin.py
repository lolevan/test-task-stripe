from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    """Class for customized admin panel"""
    list_display = ('id', 'name', 'price')
    list_display_links = ('id', 'name')
    list_editable = ('price',)


admin.site.register(Item, ItemAdmin)
