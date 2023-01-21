from rest_framework.serializers import ModelSerializer,SerializerMethodField,StringRelatedField

from roomsapp.models import Room,Message

class base_room_ser(ModelSerializer):
    users_count=SerializerMethodField()
    class Meta:
        model=Room
        fields=['id','name','owner','users_count','image','addtime']
    def get_users_count(self,obj):
        return obj.users.count()
class base_message_ser(ModelSerializer):
    class Meta:
        model = Message
        fields='__all__'

