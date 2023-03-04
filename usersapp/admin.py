from django.contrib import admin
from .models import Users
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',  'is_superuser')
    search_fields = ('id', 'name', 'email')
    list_filter = ( 'is_superuser',)

admin.site.register(Users, UserAdmin)