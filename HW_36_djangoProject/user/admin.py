from django.contrib import admin
from django.contrib.auth import get_user_model

# admin.site.register(get_user_model())

@admin.register(get_user_model())
class UserAdmin(admin.ModelAdmin):
    empty_value_display = 'No data',
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'age', 'is_superuser', 'is_active')
    list_filter = ('last_name', )
    list_editable = ('first_name', 'last_name')
    ordering = ('username', )
    readonly_fields = ('username', )
    search_fields = ('user_name', 'last_name')
    list_display_links = ('id', 'username', 'email', 'age')
