from django.contrib import admin
from book.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'title', 'year', 'price')
    list_filter = ('author', 'title')
    list_editable = ('year', 'price')
    ordering = ('author', )
    search_fields = ('title', 'author')
    list_display_links = ('id', 'author', 'title')