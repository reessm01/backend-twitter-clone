from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.Notifications.models import Notifications

@login_required
def notifications(request, *args, **kwargs):
    u = request.user
    _TwitterUser = TwitterUser.objects.get(user=u)
    _Notifications = Notifications.objects.filter(owner=_TwitterUser).order_by('-created_at')
    page = 'notifications.html'

    return render(request, page, {'all_notifications': _Notifications, 'user': u})

def get_notifications(_TwitterUser):
    return Notifications.objects.filter(owner=_TwitterUser, seen=False)