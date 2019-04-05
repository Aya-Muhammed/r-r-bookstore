from django.contrib import admin
from .models import Accessory


class AccessoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'category')
    list_filter = ('category', 'price',)
    list_editable = ('category',)
    search_fields = ('category', 'name',)
    list_per_page = 25


admin.site.register(Accessory, AccessoryAdmin)
