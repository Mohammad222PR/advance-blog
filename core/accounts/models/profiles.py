from django.db import models
from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.contrib.auth import get_user_model

User = get_user_model()




    
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=100, default='nome firstname', blank=True, null=True)
    last_name = models.CharField(max_length=100, default='nome lastname', blank=True, null=True)
    email = models.EmailField(max_length=100)
    avatar = models.ImageField(upload_to='images/profile', blank=True, null=True)
    bio = models.TextField(max_length=10000000)
    created_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.email
    

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)