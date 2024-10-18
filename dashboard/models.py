from django.db import models
from django.contrib.auth.models import AbstractUser

class User_Details(AbstractUser):
    
    age = models.IntegerField(null=True, blank=True) 

    

    def __str__(self):
        
        return self.first_name
    

