
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=250, verbose_name='Фамилия')
    name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Отчество')
    email = models.EmailField(unique=True, verbose_name='Электронная почта')  
    created_at = models.DateTimeField(auto_now_add=True)
    profile_pictures = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)



    def __str__(self):
        return self.username