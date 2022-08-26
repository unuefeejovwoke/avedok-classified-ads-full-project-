from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    short_intro = models.CharField(max_length=200, blank=True, null=True)
    bio = models.CharField(max_length=200, blank=True, null=True)
    whatsapp = models.CharField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='profile_pics',default='default.jpeg')
    phone = models.CharField(max_length=17)
    

    def __str__(self):
        return f'{self.user.username} Profile'