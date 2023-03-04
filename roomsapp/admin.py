from django.contrib import admin
from.models import Room,Message
from .forms import RoomForm

class RoomAdmin(admin.ModelAdmin):
    form = RoomForm
    list_display = ['id','name', 'password', 'image','users_count']
    search_fields = ['name']
    readonly_fields = ['id','addtime']
    fieldsets = (
        (None, {
            'fields': ('name', 'password', 'image')
        }),
    )

class MessageAdmin(admin.ModelAdmin):
     list_display=('sender','text','image','room_id','sendtime')
    

admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
