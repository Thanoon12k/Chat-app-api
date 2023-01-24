from django.urls import path

from . import views


urlpatterns = [
    path("chat", views.index, name="index"),
    path("sync_rooms/<str:room_name>/", views.room, name="room"),
    path("async_rooms/<str:room_name>/", views.room, name="room"),
    path("rest_rooms/<str:room_name>/", views.room, name="room"),
]