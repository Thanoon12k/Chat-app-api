from rest_framework.serializers import ModelSerializer,SerializerMethodField,StringRelatedField,DateTimeField,ImageField

from roomsapp.models import Room
from usersapp.models import Users,Notification,Comments


class base_user_ser(ModelSerializer):
    class Meta:
        model=Users
        fields=['id','name','email']


class user_comments_ser(ModelSerializer):
    sendtime = DateTimeField(format='%a , %I:%M %p',read_only=True)
    sender_name=StringRelatedField(source='sender')
    class Meta:
        model=Comments
        fields=['id','sender','sender_name','reception','text','image','sender_image','sendtime']


class user_view_ser(ModelSerializer):
    user_comments = user_comments_ser(many=True)

    class Meta:
        model=Users
        fields=['id','name','status','image','stars','user_comments']

class user_stars_ser(ModelSerializer):
    class Meta:
        model=Users
        fields=['id','stars']
