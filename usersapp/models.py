from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext 
from django.utils import timezone
from .managers import UserManager

class Users(AbstractUser):
    email               = models.EmailField(null=True,blank=True, verbose_name='البريد الالكتروني ',max_length=255  )
    name                = models.CharField(unique=True,blank=False,null=False ,max_length=100,verbose_name='الاسم')
    birthdate           = models.DateField(default=timezone.now,verbose_name='تاريخ الميلاد')
    image               = models.ImageField(null=True,blank=True,upload_to='profile_images',verbose_name='الصورة الشخصية')
    cover_image         = models.ImageField(null=True,blank=True,upload_to='cover_images',verbose_name='صورة الغلاف')
    token              = models.CharField(max_length=150,null=True,blank=True,verbose_name='توكن')
    notification        = models.CharField(choices=(
                                            ('no_alert','ايقاف الاشعارات'),
                                            ('just_icon','ايقونة فقط'),
                                            ('icon_image','ايقونة وصورة')
                                            ),default='icon_image',max_length=15,verbose_name='الاشعارات')
    gender              = models.CharField(choices=(('m','male'),('f','famle')),default='m',max_length=15,verbose_name='الجنس')
    comments            = models.BooleanField(default=False,verbose_name='التعليفات')
    private             = models.BooleanField(default=False,verbose_name='الخاص')
    status              = models.CharField(max_length=25,default='-',verbose_name='الحالة')
    is_banned           = models.BooleanField(default=False,verbose_name='حالة الحضر')
    is_admin            = models.BooleanField(default=False,verbose_name='ادمن')
    stars               =models.IntegerField(default=0)
    ip                  = models.CharField(blank=True,null=True ,max_length=100,verbose_name='الأي بي')
    mac                 = models.CharField(blank=True,null=True ,max_length=100,verbose_name='الماك')
    

    USERNAME_FIELD = 'name'
    objects = UserManager()
    def __str__(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
      return self.is_admin
    def has_module_perms(self, app_label):
        return True
    @property
    def is_staff(self):
        return self.is_admin
    @property
    def first_name(self):
        return self.name
    @property
    def username(self):
        return self.name
    class Meta:
            verbose_name_plural='المستخدمين'


class Notification(models.Model):
    sender          = models.ForeignKey('usersapp.Users', related_name='sender_notify',on_delete=models.CASCADE,  )
    reception_id    = models.ForeignKey('usersapp.Users',blank=True,null=True, on_delete=models.SET_NULL, related_name='recieption_notify', )
    room_id         = models.ForeignKey('roomsapp.Room',blank=True,null=True, on_delete=models.SET_NULL, related_name='room_notify', )
    token            = models.CharField(blank=True,null=True,max_length=200)
    url             =models.CharField(max_length=150,blank=True)
    is_read          = models.BooleanField(default=False)
    title            = models.CharField(blank=True,null=True,max_length=100,default='title --')
    body     = models.TextField(blank=True,null=True,default='desc --')
    addtime       = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-id']
        verbose_name_plural='الاشعارات'
    def __str__(self):
        return str(self.title)


class Comments(models.Model):
    reception       = models.ForeignKey(Users, on_delete=models.CASCADE,related_name='user_comments',verbose_name='المستلم')
    sender          = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='comment_sender',verbose_name='المرسل')
    text            = models.CharField(max_length=200, blank=True,verbose_name='الرسالة')
    token           = models.CharField(blank=True,null=True,max_length=200,verbose_name='توكن')
    image           = models.ImageField(upload_to='comments_images',verbose_name='الصورة',null=True,blank=True)    
    sendtime        = models.DateTimeField(auto_now_add=True,verbose_name='تاريخ الأنشاء')

    class Meta:
        verbose_name_plural='التعليقات '

        ordering = ('-id',)
    def __str__(self):
        return f'sender: {self.sender.name} to {self.reception.name}'
    def sender_image(self):
        url='http://127.0.0.1:8000/media/'+str(self.sender.image)
      
        return url
