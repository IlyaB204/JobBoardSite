from datetime import timezone
from  django.conf import settings
from django.db import models


class Vacancy(models.Model):
    job_description = models.TextField()
    title = models.TextField(max_length=200)
    location = models.CharField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
            'users.User',
            on_delete= models.CASCADE, verbose_name='Автор'
    )

    def __str__(self):
        return self.title
