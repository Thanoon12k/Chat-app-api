from rest_framework.serializers import ModelSerializer,SerializerMethodField,StringRelatedField,DateTimeField

from roomsapp.models import Room,Message

class base_room_ser(ModelSerializer):
    class Meta:
        model=Room
        fields=['id','name','password','users_count','image','addtime']
   
class base_message_ser(ModelSerializer):
    sendtime = DateTimeField(format='%a , %I:%M %p',read_only=True)
    sender_name=StringRelatedField(source='sender')

    class Meta:
        model = Message
        fields=['id','text','sender','sender_name','room_id','image','sendtime']
