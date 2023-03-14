
from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework import status

from roomsapp.models import Room,Message
from usersapp.models import Users
from .serializers import *
from api.usersapi.serializers import base_user_ser
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




class RoomActiveMembers(generics.ListAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_user_ser
    def get_queryset(self,pk=None,*args,**kwargs):
        pk=self.kwargs['pk']
        room=Room.objects.filter(id=pk).first()
        if room:
            return room.users.all()
        return Room.objects.none()

class RoomBannedMembers(generics.ListAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_user_ser
    def get_queryset(self,pk=None,*args,**kwargs):
        room=get_object_or_404(Room,id=self.kwargs['pk'])
        return room.banned_users.all()

class RoomAddMember(generics.CreateAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_user_ser
    def post(self,*args,**kwargs):
        room=get_object_or_404(Room,id=kwargs['pk'])
        user=get_object_or_404(Users,id=kwargs['user_id'])
        room.users.add(user)
        return Response(f'user {user} add to room {room}')

class RoomBanMember(generics.CreateAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_user_ser
    def post(self,*args,**kwargs):
        room=get_object_or_404(Room,id=kwargs['pk'])
        user=get_object_or_404(Users,id=kwargs['user_id'])
        room.banned_users.add(user)
        return Response(f'banned successfully',200)

class RoomSetMemberAdmin(generics.CreateAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_user_ser
    def post(self,*args,**kwargs):
        room=get_object_or_404(Room,id=kwargs['pk'])
        user=get_object_or_404(Users,id=kwargs['user_id'])
        room.admin_users.add(user)
        return Response(f'set admin successfully',200)

class RoomKickMember(generics.CreateAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_user_ser
    def post(self,*args,**kwargs):
        room=get_object_or_404(Room,id=kwargs['pk'])
        user=get_object_or_404(Users,id=kwargs['user_id'])
        room.users.remove(user)
        room.admin_users.remove(user)
        return Response(f'kicked successfully',200)
