from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.
#wDjango provides two ways for us to implement custom user model. Abstract User Class or Abstract Base Class. Abstract User Class allows you to add on top of what the django and user model already have. extra fields.
#Abstract Based Class: when we want to build own user model from scratch from bare bones we use abstract base class
#WE ARE USING ABSTRACT BASED CLASS HERE AS WE ARE BUILDING FROM SCRATCH

class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(max_length=255, unique=True, verbose_name=_("Email Address"))
    first_name=models.CharField(max_length=100,verbose_name=_("First Name"))
    last_name=models.CharField(max_length=100, verbose_name=_("Last Name"))
    