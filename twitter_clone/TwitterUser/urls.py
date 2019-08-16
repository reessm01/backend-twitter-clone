from django.contrib import admin
from django.urls import path

from twitter_clone.TwitterUser.models import TwitterUser
admin.site.register(TwitterUser)

url_patterns = [
]