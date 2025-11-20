from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class OtherDetails(AbstractUser):
    user_city = models.CharField(max_length=50)
    user_contact = models.CharField(max_length=10)
    
    def __str__(self):
        return self.username