from django.db import models

class Picture(models.Model):
    description = models.TextField()  # Field for the picture's description
    image = models.ImageField(upload_to='pictures/')  # Field for the image

    def __str__(self):
        return self.description  # This will show the description in the admin interface
    

from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score1 = models.JSONField(default=list)
    score2 = models.JSONField(default=list)
    score3 = models.JSONField(default=list)

    def __str__(self):
        return self.user.username
    
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
