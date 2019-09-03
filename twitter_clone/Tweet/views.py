import re

from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.views.generic import TemplateView

from twitter_clone.Tweet.forms import NewTweetForm

from twitter_clone.Tweet.models import Tweet
from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.Notifications.models import Notifications
from twitter_clone.Notifications.views import get_notifications

@login_required
def new_tweet(request, *args, **kwargs):
    if request.method == 'POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = request.user
            if u is not None:
                tweet = Tweet.objects.create(
                text=data['text'],
                author=TwitterUser.objects.get(user=u)
                )
                process_mentions(tweet, u)
            else:
                page = 'timeline.html'
                tweet_error_message = 'Oops something went wrong!'
                form = NewTweetForm()
                return render(request, page, {'form': form, 'tweet_error_message': tweet_error_message})

            return HttpResponseRedirect(reverse('homepage'))

class ATweet(TemplateView):
    def get(self, request, *args, **kwargs):
        id = request.GET.get('id')
        tweet = Tweet.objects.get(id=id)
        page = 'single_tweet.html'
        u = False
        _Notifications = False
        not_logged_in = False
        if not request.user.is_anonymous:
            u = request.user
            _TwitterUser = TwitterUser.objects.get(user=u)
            _Notifications = get_notifications(_TwitterUser)
        else:
            not_logged_in = True
        if _Notifications:
            related_notification = _Notifications.filter(mentions=tweet).all()[0]
            if related_notification and related_notification.owner.user.username == _TwitterUser.user.username:
                related_notification.seen = True
                related_notification.save()
                _Notifications = get_notifications(_TwitterUser)

        return render(request, page, {'tweet': tweet, 'notifications': _Notifications, 'user': u, 'not_logged_in': not_logged_in})

def process_mentions(tweet, user):
    pattern = re.compile(r'@([A-Za-z0-9_]+[A-Za-z0-9_]+)')
    if '@' in tweet.text:
        matches = re.findall(pattern, tweet.text)

        for match in matches:
            if user.username != match:
                u = TwitterUser.objects.filter(user__username = match)
                if u:
                    _Notification = Notifications.objects.create(
                        owner=u[0]
                    )
                    _Notification.mentions.add(tweet)
