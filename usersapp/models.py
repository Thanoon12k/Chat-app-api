from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext 
from django.utils import timezone
from .managers import UserManager

class Users(AbstractUser):
    email               = models.EmailField(null=True,blank=True, verbose_name='Email Address',max_length=255  )
    name                = models.CharField(unique=True,blank=False,null=False ,max_length=100)
    birthdate           = models.DateField(default=timezone.now)
    image               = models.ImageField(null=True,blank=True,upload_to='profile_images')
    cover_image         = models.ImageField(null=True,blank=True,upload_to='cover_images')
    gender              = models.CharField(choices=(('m','male'),('f','famle')),default='m',max_length=15)
    status              = models.CharField(max_length=25,default='-')
    comments            = models.BooleanField(default=False)
    private             = models.BooleanField(default=False)
    notification        = models.BooleanField(default=False)
    is_banned           = models.BooleanField(default=False)
    is_admin            = models.BooleanField(default=False)
    ip               = models.CharField(blank=True,null=True ,max_length=100)
    mac                = models.CharField(blank=True,null=True ,max_length=100)
    

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
    