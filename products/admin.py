from django.contrib import admin
from . models import Item

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']

    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)