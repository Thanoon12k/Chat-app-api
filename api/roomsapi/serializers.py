from rest_framework.serializers import ModelSerializer,SerializerMethodField

from roomsapp.models import Room,Message

class rooms_list_ser(ModelSerializer):
    class Meta:
        model=Room
        fields='__all__'

class room_messages_ser(ModelSerializer):
    class Meta:
        model = Message
        fields='__all__'

