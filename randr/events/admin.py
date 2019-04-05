from django.contrib import admin
from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'time', 'location')
    list_filter = ('date',)
    list_editable = ('date', 'time')
    search_fields = ('location', 'name',)
    list_per_page = 25


admin.site.register(Event, EventAdmin)

