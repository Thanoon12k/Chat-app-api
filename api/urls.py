from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


from django.urls import path
from api.roomsapi.views import *
from api.usersapi.views import *
from .views import ListAppUrls
RootUrls=[
        path('',ListAppUrls.as_view(),name='list-app-urls') ,
        ]
RoomsUrls=[
        
    path('rooms/',ListRooms.as_view(),name='list-rooms') ,
    path('rooms/new',CreateRoom.as_view(),name='new-room') ,
    path('rooms/detail/<int:pk>',DetailRoom.as_view(),name='detail-room') ,
    
    path('rooms/<int:pk>/messages',ListMessages.as_view(),name='list-messsages') ,
    path('rooms/<int:pk>/messages/new',CreateMessage.as_view(),name='new-messages') ,
    path('rooms/<int:pk>/messages/<int:msg_id>',DetailMessage.as_view(),name='detail-message') ,
        
        ]

UsersUrls=[
        
        path('rooms/<int:pk>/active_users',RoomActiveMembers.as_view(),name='room-active-members-list') ,
        path('rooms/<int:pk>/banned_users',RoomBannedMembers.as_view(),name='room-banned-members-list') ,
        path('rooms/<int:pk>/add_member/<int:user_id>',RoomAddMember.as_view(),name='new-member') ,
        path('rooms/<int:pk>/set_member_admin/<int:user_id>',RoomSetMemberAdmin.as_view(),name='set-member-admin') ,
        path('rooms/<int:pk>/ban_member/<int:user_id>',RoomBanMember.as_view(),name='ban-member') ,
        path('rooms/<int:pk>/kick_member/<int:user_id>',RoomKickMember.as_view(),name='kick-member') ,
          
           ]

LiveUrls=[

        # path('rooms-live/',LiveRooms.as_asgi(),name='list-rooms') ,
    

]
DocsUrls=[

      path('docs/',include_docs_urls(title='IRAQ CHAT APP')),
      path('swagger',get_swagger_view(title='IRAQ CHAT APP')),
      path('shema',get_schema_view(title='IRAQ CHAT APP', description='api for iraq chat app website', version='1.0.0',)
                                           ,name='Schema')


]



urlpatterns=RootUrls+RoomsUrls+LiveUrls+UsersUrls+DocsUrls