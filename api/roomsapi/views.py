
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework import status

from roomsapp.models import Room,Message
from usersapp.models import Users
from .serializers import *
from ..firebase import SendMessage


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
        room_id=kwargs['pk']
        sender=request.POST.get('sender')
        sender_name=request.POST.get('sender_name')
        text=request.POST.get('text')
        attachment=request.POST.get('attachment')
        sendtime=request.POST.get('sendtime')
        print('room_id : ',room_id)
        print('sender : ',sender)
        print('sender_name : ',sender_name)
        print('text : ',text)
        print('attachment : ',attachment)
        print('sendtime : ',sendtime)
        SendMessage(id, sender, sender_name, room_id, text, sendtime)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    