from django.contrib import admin
from .models import Users,Notification
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',  'is_superuser')
    search_fields = ('id', 'name', 'email')
    list_filter = ( 'is_superuser',)

class notifyadmin(admin.ModelAdmin):
    list_display=('id','sender','room_id','reception_id','title','body')

admin.site.register(Users, UserAdmin)
admin.site.register(Notification, notifyadmin)