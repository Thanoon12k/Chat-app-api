from rest_framework.serializers import ModelSerializer
from usersapp.models import Notification

class user_notify_ser(ModelSerializer):
   class Meta:
      model=Notification
      fields=['id','sender','reception_id','room_id','token','title','body','is_read','addtime']
     
