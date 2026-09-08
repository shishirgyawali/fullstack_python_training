from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from .managers import UserManager

# Create your models here.
#wDjango provides two ways for us to implement custom user model. Abstract User Class or Abstract Base Class. Abstract User Class allows you to add on top of what the django and user model already have. extra fields.
#Abstract Based Class: when we want to build own user model from scratch from bare bones we use abstract base class
#WE ARE USING ABSTRACT BASED CLASS HERE AS WE ARE BUILDING FROM SCRATCH

class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=255, unique=True, verbose_name=_("Email Address"))
    first_name=models.CharField(max_length=100,verbose_name=_("First Name"))
    last_name=models.CharField(max_length=100, verbose_name=_("Last Name"))
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    last_login=models.DateTimeField(auto_now=True)

    USERNAME_FIELD="email"

    REQUIRED_FIELDS=["first_name","last_name"]

    objects=UserManager()

    def __str__(self):
        return self.email
    
    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def tokens(self):
        pass


class OneTimePassword(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, unique=True)

    def __str__(self):
        return f"OTP for {self.user.first_name}: {self.code}-passcode"