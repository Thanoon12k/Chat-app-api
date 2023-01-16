from rest_framework.serializers import ModelSerializer,SerializerMethodField

from roomsapp.models import Room
from usersapp.models import Users

class roomusers_list_ser(ModelSerializer):
    class Meta:
        model=Users
        fields='name'
