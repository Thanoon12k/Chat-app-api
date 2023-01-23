from django.urls import re_path,path

from .async_cons import async_msg
from .sync_cons import   sync_msg

ws_urlpatterns = [
    path("rooms/<room_name>/", sync_msg.as_asgi(),name='messages-manager'),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    # path("ws/chat/<room_name>/", ChatConsumer.as_asgi()),
    



]