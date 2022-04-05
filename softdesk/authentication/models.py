from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=128, null=True)
    USERNAME_FIELD = 'email'

    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    REQUIRED_FIELDS = ['username']
