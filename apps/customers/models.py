from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPES = [
        ('customer', 'Customer'),
        ('tenants', 'Tenant'),
    ]
    user_type = models.CharField(max_length=15, choices=USER_TYPES, default='customer')