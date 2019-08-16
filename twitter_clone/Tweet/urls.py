from django.contrib import admin
from django.urls import path

from twitter_clone.Tweet.models import Tweet
admin.site.register(Tweet)

url_patterns = [
]