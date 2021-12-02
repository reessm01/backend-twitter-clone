from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic import TemplateView

from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.Notifications.models import Notifications

class ANotifications(TemplateView):
    def get(self, request, *args, **kwargs):
        u = request.user
        _TwitterUser = TwitterUser.objects.get(user=u)
        _Notifications = Notifications.objects.filter(owner=_TwitterUser).order_by('-created_at')
        page = 'notifications.html'

        return render(request, page, {'all_notifications': _Notifications, 'user': u})

def get_notifications(_TwitterUser):
    return Notifications.objects.filter(owner=_TwitterUser, seen=False)