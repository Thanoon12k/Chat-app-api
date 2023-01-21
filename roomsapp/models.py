from django.db import models
from usersapp.models import Users
class Room(models.Model):
    owner           = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True, related_name="room_owner"  )

    name            =models.CharField(max_length=50)
    slug            =models.CharField(max_length=50,blank=True,null=True)
    password        =models.CharField(max_length=25)
    admins_password        =models.CharField(max_length=25)
    image               = models.ImageField(null=True,blank=True,upload_to='rooms_images')
    
    users           =models.ManyToManyField(Users,blank=True,related_name='room_users')
    admin_users           =models.ManyToManyField(Users,blank=True,related_name='room_admins')
    banned_users           =models.ManyToManyField(Users,blank=True,related_name='room_banned_users')
    addtime = models.DateTimeField(auto_now_add=True)
    
    class Meta:
            ordering = ('-id',)
    def __str__(self):
        return self.name
    def save(self,*args,**kwargs):
        self.slug=self.name
        return super().save(args,kwargs)
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