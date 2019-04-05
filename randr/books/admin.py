from django.contrib import admin

from .models import Book, PublishHouse, Author


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'price', 'classification', 'publish_house',
                    'is_available', 'book_date', 'is_best_selling')
    list_filter = ('author', 'publish_house',)
    list_editable = ('is_available', 'is_best_selling')
    search_fields = ('classification', 'author__name', 'publish_house__name',)
    list_per_page = 25


admin.site.register(Book, BookAdmin)
admin.site.register(PublishHouse)
admin.site.register(Author)
