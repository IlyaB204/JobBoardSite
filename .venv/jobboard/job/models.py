from datetime import timezone

from django.db import models

class JobModel(models.Model):
    job_description = models.TextField()
    title = models.TextField(max_length=200)
    location = models.CharField(max_length=250)
    publish_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
