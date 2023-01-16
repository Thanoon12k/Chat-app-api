
from rest_framework import generics,permissions
from roomsapp.models import Room
from usersapp.models import Users
from .serializers import *




class UsersList(generics.ListAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    serializer_class=roomusers_list_ser
    def get_queryset(self,pk=None,*args,**kwargs):
        pk=self.kwargs['pk']
        return Room.objects.filter(id=pk)