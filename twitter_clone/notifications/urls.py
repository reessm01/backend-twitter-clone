from django.contrib import admin
from django.urls import path

from twitter_clone.Notifications.models import Notifications
admin.site.register(Notifications)

url_patterns = [
]