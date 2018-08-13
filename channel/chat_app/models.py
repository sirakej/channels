from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Channel(models.Model):
    name = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    message = models.TextField()
    channel = models.ForeignKey(Channel,on_delete=models.CASCADE)
    post = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, null=True , on_delete=models.CASCADE)

    def __str__(self):
        return self.message
