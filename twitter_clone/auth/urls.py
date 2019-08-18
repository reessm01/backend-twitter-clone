from django.urls import path

from twitter_clone.auth.views import *

url_patterns = [
    path('login/', login_view, name='login'),
    path('register', register_view, name='register'),
    path('logout', logout, name='logout')
]