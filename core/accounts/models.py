from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
    )


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extera_fields):
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
            raise ValueError(_("staff user most be not True"))
        
        if extera_fields.get('is_superuser') is not True:
            raise ValueError(_("super user most be not True"))
        self.create_user(email, password, **extera_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"
    

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin