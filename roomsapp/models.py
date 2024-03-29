from django.db import models
from usersapp.models import Users



class Room(models.Model):
    owner           = models.ForeignKey(Users, on_delete=models.SET_NULL,blank=True, null=True, related_name="room_owner" ,verbose_name='المؤسس' )
    name            =models.CharField(max_length=50,verbose_name='اسم الغرفة')
    password        =models.CharField(max_length=25,verbose_name='كلمة المرور',default='0')
    admins_password        =models.CharField(max_length=25,null=True)
    image               = models.ImageField(upload_to='rooms_images',verbose_name='الصورة')    
    users           =models.ManyToManyField(Users,blank=True,related_name='room_users',verbose_name='الأعضاء')
    admin_users           =models.ManyToManyField(Users,blank=True,related_name='room_admins',verbose_name='المسؤلين')
    banned_users           =models.ManyToManyField(Users,blank=True,related_name='room_banned_users',verbose_name='الاعضاء المحضورين')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name='تاريخ الانشاء')
    
    class Meta:
            verbose_name_plural='الغرف'
            ordering = ('id',)
    def __str__(self):
        return self.name
    def users_count(self):
        return self.users.count()
    users_count.short_description = 'عدد المستخدمين'

class Message(models.Model):
    sender = models.ForeignKey(Users, on_delete=models.SET_NULL,null=True, related_name='message_sender',verbose_name='المرسل')
    text = models.CharField(max_length=200, blank=True,verbose_name='الرسالة')
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE,verbose_name='الغرفة')
    token            = models.CharField(blank=True,null=True,max_length=200,verbose_name='توكن')

    image               = models.ImageField(upload_to='message_images',verbose_name='الصورة',null=True)    
    sendtime = models.DateTimeField(auto_now_add=True,verbose_name='تاريخ الأنشاء')

    class Meta:
        verbose_name_plural='الدردشات '

        ordering = ('-id',)
    def __str__(self):
        return self.text[0:10]+' ...'

class Bans(models.Model):
    user = models.ForeignKey(Users, on_delete=models.SET_NULL,null=True, verbose_name='الاسم')
    room = models.CharField(max_length=200, blank=True,null=True, verbose_name='الغرفة')
    addtime = models.DateTimeField(auto_now_add=True,verbose_name='تاريخ الحضر')


    class Meta:
        verbose_name_plural='الاشخاص المحضوررين '

        ordering = ('-id',)
    def __str__(self):
        return str(self.user)
