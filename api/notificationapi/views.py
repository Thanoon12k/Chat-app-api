from django.http import Http404
from rest_framework import generics,permissions
from rest_framework.response import Response
from .serializers import user_notify_ser
from usersapp.models import Notification


class UserNotify(generics.ListAPIView):
    """list of all user notification"""
    permission_classes=[permissions.BasePermission]
    serializer_class=user_notify_ser
    def get_queryset(self): 
        return Notification.objects.filter(recipient=self.request.user)

class AllNotification(generics.ListAPIView):
    """list of all  notification"""
    permission_classes=[permissions.BasePermission]
    serializer_class=user_notify_ser
    queryset=Notification.objects.all()
class LastNotify(generics.RetrieveAPIView):
    """ return last not read notify for user """
    
    permission_classes=[permissions.BasePermission]
    serializer_class=user_notify_ser
    def get_object(self):
        last_notify=Notification.objects.filter(recipient=self.request.user,is_read=True).first()
        if last_notify:
            return last_notify
        raise Http404()

class NotifySetRead(generics.UpdateAPIView):
    """ set notify as read """
    permission_classes=[permissions.BasePermission]
    serializer_class=user_notify_ser
    queryset=Notification.objects.all()

class NotifyDestroy(generics.DestroyAPIView):
    """delete current notify """
    permission_classes=[permissions.BasePermission]
    serializer_class=user_notify_ser
    queryset=Notification.objects.all()   

