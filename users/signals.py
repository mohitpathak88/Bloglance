# Signals is created so that whenever the user creates profile, it gets save automatically 

from django.db.models.signals import post_save
from django.contrib.auth.models import User   #to send the signal
from django.dispatch import receiver          #to recieve the signal
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):       #kwargs accepts any additional keyword
    instance.profile.save()