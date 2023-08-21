from django.contrib import admin
from purchase.models import Purchase

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'book_id', 'get_book_full_name', 'get_user_full_name')
    ordering = ('date', )
    search_fields = ('book_id', )
    list_display_links = ('id', 'date', 'get_book_full_name', 'get_user_full_name')

    def get_user_full_name(self, obj):
        return obj.user.get_full_name()

    get_user_full_name.short_description = 'User mame'

    def get_book_full_name(self, obj):
        return obj.book.author +' ' + obj.book.title

    get_book_full_name.short_description = 'Book mame'