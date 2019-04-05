from django.contrib import admin
from .models import Store


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'location')
    list_filter = ('location',)
    list_editable = ('phone', 'location')
    search_fields = ('location', 'name',)
    list_per_page = 25


admin.site.register(Store, StoreAdmin)


