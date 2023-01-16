
from rest_framework import generics,permissions
from roomsapp.models import Room,Message

from .serializers import *




class RoomsList(generics.ListAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=rooms_list_ser
    queryset=Room.objects.all()
class RoomMessagesList(generics.ListAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=room_messages_ser
    queryset=Message.objects.all()