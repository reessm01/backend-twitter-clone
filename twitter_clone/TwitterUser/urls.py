from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.TwitterUser.views import user_profile, unfollow, find, Follow

url_patterns = [
    path('profile/', user_profile, name='username'),
    path('follow/', login_required(Follow.as_view())),
    path('unfollow/', unfollow),
    path('find', find)
]