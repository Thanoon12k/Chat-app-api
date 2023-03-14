from django.contrib import admin
from .models import Users,Notification,Comments
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','status', 'stars')
    search_fields = ('id', 'name', 'email')
    list_filter = ( 'is_superuser',)

class notifyadmin(admin.ModelAdmin):
    list_display=('id','sender','room_id','reception_id','title','body')
class comments_admin(admin.ModelAdmin):
    list_display=('reception','sender','text','image','token','id')

admin.site.register(Users, UserAdmin)
admin.site.register(Notification, notifyadmin)
admin.site.register(Comments, comments_admin)