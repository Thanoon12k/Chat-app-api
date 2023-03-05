
from rest_framework import generics,permissions
from rest_framework.authtoken.models import Token

from rest_framework.response import Response
from roomsapp.models import Room
from usersapp.models import Users
from .serializers import *
from django.shortcuts import get_object_or_404

 
class UserRegister(generics.CreateAPIView):
    """ list of all rooms """
    permission_classes=[permissions.BasePermission]
    queryset=Users.objects.all()
    serializer_class=user_register_ser

   
  