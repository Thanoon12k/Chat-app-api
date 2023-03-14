
from rest_framework import generics,permissions
from rest_framework.response import Response
from roomsapp.models import Room
from usersapp.models import Users
from .serializers import *
from django.shortcuts import get_object_or_404


class UsersView(generics.RetrieveAPIView):
    """ set notify as read """
    permission_classes=[permissions.BasePermission]
    serializer_class=user_view_ser
    queryset=Users.objects.all()
class AddComment(generics.CreateAPIView):
    """ set notify as read """
    permission_classes=[permissions.BasePermission]
    serializer_class=user_comments_ser
    queryset=Comments.objects.all()
class RemoveComment(generics.DestroyAPIView):
    """ set notify as read """
    permission_classes=[permissions.BasePermission]
    serializer_class=user_comments_ser
    queryset=Comments.objects.all()
   
class StarsUpdate(generics.UpdateAPIView):
    """ set notify as read """
    permission_classes=[permissions.BasePermission]
    serializer_class=user_stars_ser
    queryset=Users.objects.all()
