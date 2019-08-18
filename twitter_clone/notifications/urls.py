from django.contrib import admin
from django.urls import path

from twitter_clone.Notifications.models import Notifications
admin.site.register(Notifications)

from twitter_clone.Notifications.views import notifications

url_patterns = [
    path('notifications', notifications, name='notifications')
]