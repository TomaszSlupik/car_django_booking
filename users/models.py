from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class User (AbstractBaseUser):
    name = models.CharField(max_length=50, unique=True)
    token = models.CharField(max_length=500, blank=True, null=True)

