import profile
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)
    
        subject = 'Welcome to Avedok Classified Ads Website'
        message = 'Glad to have you!, Please edit your profile and enjoying posting ads'
            
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [instance.email],
            fail_silently=False,
        )

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    
    instance.profile.save()