from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = "permissionapp_user"
        verbose_name = "admin用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username