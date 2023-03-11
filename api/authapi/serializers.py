from rest_framework.serializers import ModelSerializer,SerializerMethodField,StringRelatedField,CharField;
from rest_framework.authtoken.models import Token

from roomsapp.models import Room
from usersapp.models import Users

class user_register_ser(ModelSerializer):
    token=SerializerMethodField()
    class Meta:
        model=Users
        fields=['id','name','status','notification','image','token']
    def get_token(self,obj):
        user=Users.objects.last()
        token,create=Token.objects.get_or_create(user=user)
        return token.key

class user_update_ser(ModelSerializer):
    class Meta:
        model=Users
        fields=['id','name','status','birthdate','gender','image','comments','private','notifications']
    
class user_logout_ser(ModelSerializer):
    class Meta:
        model=Users
        fields=['id','is_active']
    

