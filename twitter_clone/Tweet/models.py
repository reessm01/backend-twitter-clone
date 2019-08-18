from django.db import models
from django.contrib.auth.models import User
from twitter_clone.TwitterUser.models import TwitterUser

class Tweet(models.Model):
    text = models.CharField(max_length=140)
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='author')
    likes = models.ManyToManyField(TwitterUser)
    created_at = models.DateTimeField(auto_now_add=True)