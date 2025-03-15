from django.contrib.auth.models import AbstractUser
from django.db import models

class User (AbstractUser):
    first_name = models.CharField(max_length=250, verbose_name='Фамилия')
    last_name = models.CharField(max_length=250, verbose_name='Имя')
    patronymic = models.CharField(max_length=250, verbose_name='Отчество')
    email = models.EmailField()
    published_date = models.DateField()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'patronymic', 'email', 'published_date']

    def __str__(self):
        return self.username

