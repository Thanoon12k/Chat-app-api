from django.db import models
from usersapp.models import Users
class Room(models.Model):
    owner           = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name="room_owner"  )
    name            =models.CharField(max_length=50)
    password        =models.CharField(max_length=15)
    users           =models.ManyToManyField(Users,blank=True)
    addtime = models.DateTimeField(auto_now_add=True)

    class Meta:
            ordering = ('-id',)
    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.SET_NULL,null=True, related_name='message_sender')
    text = models.CharField(max_length=200, blank=True)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE,)
    attachment = models.FileField(blank=True)
    addtime = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-id',)
    def __str__(self):
        return self.text[0:10]