from django.db import models
from django.db.models.signals import post_save 
from django.dispatch import receiver
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
    )


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extera_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")
        email=self.normalize_email(email)
        user = self.model(email=email, **extera_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extera_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """

        extera_fields.setdefault('is_staff',True)
        extera_fields.setdefault('is_superuser',True)
        extera_fields.setdefault('is_active',True)

        if extera_fields.get('is_staff') is not True:
            raise ValueError("staff user most be not True")
        
        if extera_fields.get('is_superuser') is not True:
            raise ValueError("super user most be not True")
        self.create_user(email, password, **extera_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    

    
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