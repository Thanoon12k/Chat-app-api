from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view


from django.urls import path
from .views import Root
from api.roomsapi.views import *
from api.usersapi.views import *
from api.authapi.views import *
from api.notificationapi.views import *

AuthUrls=[
        path('',Root,name='rootpage'),
        path('users/user_register',UserRegister.as_view(),name='create-new-account') ,
        path('users/<int:pk>/user_ret_update',UserReteriveUpdate.as_view(),name='user-reterive-update-account') ,
        path('users/<int:pk>/user_logout',UserLogOut.as_view(),name='logout-user-account') ,
       ]
RoomsUrls=[
    path('rooms/',ListRooms.as_view(),name='list-rooms') ,
    path('rooms/<int:pk>/messages',ListMessages.as_view(),name='list-messsages') ,
    path('rooms/<int:pk>/messages/new',CreateMessage.as_view(),name='new-messages') ,
]
MembersUrls=[
        path('rooms/<int:pk>/active_users',RoomActiveMembers.as_view(),name='room-active-members-list') ,
        path('rooms/<int:pk>/banned_users',RoomBannedMembers.as_view(),name='room-banned-members-list') ,
        path('rooms/<int:pk>/add_member/<int:user_id>',RoomAddMember.as_view(),name='new-member') ,
        path('rooms/<int:pk>/set_member_admin/<int:user_id>',RoomSetMemberAdmin.as_view(),name='set-member-admin') ,
        path('rooms/<int:pk>/ban_member/<int:user_id>',RoomBanMember.as_view(),name='ban-member') ,
        path('rooms/<int:pk>/kick_member/<int:user_id>',RoomKickMember.as_view(),name='kick-member') ,
          
          
        ]

UsersUrls=[
        path('users/<int:pk>/view/',UsersView.as_view(),name='user-view-account') ,
        path('users/add_comment',AddComment.as_view(),name='user-view-account') ,
        path('users/<int:pk>/remove_comment',RemoveComment.as_view(),name='user-view-account') ,
        path('users/stars_update',StarsUpdate.as_view(),name='user-view-account') ,
        
      ]

NotifyUrls=[

            
    path('all_notification',AllNotification.as_view(),name='all-notifications'),
    path('user_notification',UserNotify.as_view(),name='user-notifications'),
    path('last_notification',LastNotify.as_view(),name='last-notifications'),
    path('notification_set_read/<int:pk>',NotifySetRead.as_view(),name='set_read-notifications'),
    path('notification_destroy/<int:pk>',NotifyDestroy.as_view(),name='set_read-notifications'),
        ]
    

        
DocsUrls=[

      path('docs',include_docs_urls(title='IRAQ CHAT APP')),
      path('swagger',get_swagger_view(title='IRAQ CHAT APP')),
      path('shema',get_schema_view(title='IRAQ CHAT APP', description='api for iraq chat app website', version='1.0.0',)
                                           ,name='Schema')


]



urlpatterns=RoomsUrls+MembersUrls+UsersUrls+AuthUrls+NotifyUrls+DocsUrls