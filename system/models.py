from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class User(AbstractUser):
    username = None
    mobile = models.CharField(max_length=14)
    email = models.EmailField(unique=True)
    is_superuser = models.BooleanField(default=False)
    is_user_role_1 = models.BooleanField(default=False)
    is_user_role_2 = models.BooleanField(default=False)
    is_user_role_3 = models.BooleanField(default=False)
    permissions = models.CharField(max_length = 225,null=True, blank=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] 
    class Meta:
        db_table = 'user'