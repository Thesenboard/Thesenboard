from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_visibility = models.CharField(max_length=40)
    user_tags = models.CharField(max_length=255)
