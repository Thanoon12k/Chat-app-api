from django.urls import path

from . import views


urlpatterns = [
    path("chat", views.index, name="index"),
    path("rooms/<str:room_name>/", views.room, name="room"),
]