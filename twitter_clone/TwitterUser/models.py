import datetime

from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    headline = models.TextField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    last_online = models.DateTimeField(auto_now_add=True)
    following = models.ManyToManyField('self', symmetrical=False, related_name='following1')
    followers = models.ManyToManyField('self', symmetrical=False, related_name='followers1')

    def __str__(self):
        return self.user.username