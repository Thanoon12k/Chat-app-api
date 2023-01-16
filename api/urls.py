from django.urls import path
from api.roomsapi.views import *
from api.usersapi.views import *

RoomsUrls=[
          path('',RoomsList.as_view(),name='rooms-list') ,
          path('messages/<int:pk>/',RoomMessagesList.as_view(),name='room-messages-list') ,
         path('users/<int:pk>/',UsersList.as_view(),name='users-list') ,
]
UsersUrls=[
        
      
           ]

urlpatterns=RoomsUrls+UsersUrls