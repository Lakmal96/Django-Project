from django.contrib import admin
from . models import Item, Size, ItemAttribute

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'status')
    list_editable = ('status',)

    class Meta:
        model = Item


admin.site.register(Item, ItemAdmin)


admin.site.register(Size)


class ItemAttributeAdmin(admin.ModelAdmin):
    list_display = ('item', 'size', 'price')

    class Meta:
        model = ItemAttribute


admin.site.register(ItemAttribute, ItemAttributeAdmin)
