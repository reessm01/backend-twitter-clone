from django.db import models
from twitter_clone.TwitterUser.models import TwitterUser

class Notifications(models.Model):
    owner = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='owner')
    new_followers = models.ManyToManyField(TwitterUser)
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)