from django.urls import path
from api.roomsapi.views import *
from api.usersapi.views import *
from .views import ListAppUrls
RootUrls=[
        path('',ListAppUrls.as_view(),name='list-app-urls') ,
        ]


RoomsUrls=[
        
    path('rooms',ListRooms.as_view(),name='list-rooms') ,
    path('rooms/new',CreateRoom.as_view(),name='new-room') ,
    path('rooms/detail/<int:pk>',DetailRoom.as_view(),name='detail-room') ,
    
    path('rooms/<int:pk>/messages',ListMessages.as_view(),name='list-messsages') ,
    path('rooms/<int:pk>/messages/new',CreateMessage.as_view(),name='new-messages') ,
    path('rooms/<int:pk>/messages/<int:msg_id>',DetailMessage.as_view(),name='detail-message') ,
        
        ]




UsersUrls=[
        
      
           ]

urlpatterns=RootUrls+RoomsUrls+UsersUrls