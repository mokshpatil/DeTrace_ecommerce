from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, PermissionsMixin, BaseUserManager
#from django.contrib.auth.base_user import BaseUserManager
#from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    is_vendor = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    wallet_balance = models.IntegerField(default=0)
    is_vendor = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username
    
"""
class CustomUserManager(BaseUserManager):

    def create_user(self, username, email, name, password, is_vendor, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, name=name, is_vendor=is_vendor, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, name, password, is_vendor, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, email, name, password, **extra_fields)
    
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(max_length=150, unique=True)
    name = models.CharField(max_length=150, blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'email']

    def __str__(self):
        return self.username

"""