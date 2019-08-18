from django.contrib import admin
from django.urls import path

from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.TwitterUser.views import user_profile, follow, unfollow, find

admin.site.register(TwitterUser)

url_patterns = [
    path('profile/', user_profile, name='username'),
    path('follow/', follow),
    path('unfollow/', unfollow),
    path('find', find)
]