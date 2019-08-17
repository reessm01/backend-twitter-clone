from django.db import models
from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.Tweet.models import Tweet

class Notifications(models.Model):
    owner = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='owner')
    new_followers = models.ManyToManyField(TwitterUser)
    mentions = models.ManyToManyField(Tweet)
    created_at = models.DateTimeField(auto_now_add=True)
    seen = models.BooleanField(default=False)