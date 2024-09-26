from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def createUser(self, name, password):
        if not name:
            raise ValueError("Użytkownik musi mieć login")
        if not password:
            raise ValueError("Użytkownik musi mieć hasło")

        user = self.model(name=name)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    name = models.CharField(max_length=50, unique=True)
    token = models.CharField(max_length=500, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = []

    def __str__(self) -> str:
        return self.name
