
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework import status

from roomsapp.models import Room,Message
from usersapp.models import Users
from .serializers import *
from ..firebase import SendMessage
import json

class ListRooms(generics.ListAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_room_ser
    queryset=Room.objects.all()

class ListMessages(generics.ListAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_message_ser
    queryset=Message.objects.all()
    def get_queryset(self):
        pk=self.kwargs['pk']
        return Message.objects.filter(room_id=pk)
    

class CreateMessage(generics.CreateAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_message_ser
    queryset=Message.objects.all()
    def create(self, request, *args, **kwargs):
        
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
      
        SendMessage(
             serializer.data['id'],
             serializer.data['sender'],
             serializer.data['sender_name'],
             serializer.data['sender_image'],
             serializer.data['room_id'],
             serializer.data['text'],
             serializer.data['image'],
             serializer.data['sendtime'])

       
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    