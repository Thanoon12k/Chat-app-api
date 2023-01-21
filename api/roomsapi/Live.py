from djangochannelsrestframework.generics import GenericAsyncAPIConsumer
from djangochannelsrestframework.mixins import (
    ListModelMixin,
    PatchModelMixin,
    UpdateModelMixin,
    CreateModelMixin,
    DeleteModelMixin,
)
from roomsapp.models import Room,Message
from rest_framework import generics,permissions
from .serializers import *

class LiveRooms(ListModelMixin, GenericAsyncAPIConsumer):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=base_room_ser
    queryset=Room.objects.all()