from django.db import models
from django.urls import reverse


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('home')
