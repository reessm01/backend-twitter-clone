from django.contrib import admin
from django.urls import path
from django.contrib.auth.decorators import login_required

from twitter_clone.Notifications.models import Notifications
admin.site.register(Notifications)

from twitter_clone.Notifications.views import ANotifications

url_patterns = [
    path('notifications', login_required(ANotifications.as_view()), name='notifications')
]