from django.contrib import admin
from django.urls import path

from twitter_clone.Tweet.models import Tweet
from twitter_clone.Tweet.views import tweet
admin.site.register(Tweet)

url_patterns = [
    path('tweet', tweet, name='tweet'),
    path('tweet/', tweet, name='post')
]