from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.views.generic import TemplateView

from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.Tweet.models import Tweet
from twitter_clone.Tweet.forms import NewTweetForm
from twitter_clone.Notifications.views import get_notifications
from twitter_clone.Notifications.models import Notifications

class HomePage(TemplateView):
    page = 'timeline.html'

    def get(self, request, *args, **kwargs):
        u = request.user
        form = NewTweetForm()
        button_label = 'Submit'
        _TwitterUser = TwitterUser.objects.get(user=u)
        _Notifications = get_notifications(_TwitterUser)
        tweet_list = []
        query = Q()
        query = query | Q(author=_TwitterUser)
        if _TwitterUser.following.all():
            for person in _TwitterUser.following.all():
                query = query | Q(author=person)
        tweet_list = Tweet.objects.filter(query).order_by('-created_at')
        
        return render(request, self.page, {'user': u, 'form': form, 'tweet_list': tweet_list, 'button_label': button_label, 'notifications': _Notifications})