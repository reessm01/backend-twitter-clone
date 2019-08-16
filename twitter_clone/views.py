from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.Tweet.models import Tweet

@login_required
def homepage(request, *args, **kwargs):
    page = 'timeline.html'
    if request.method == 'GET':
        u = request.user

        _TwitterUser = TwitterUser.objects.get(user=u)
        tweet_list = []
        if _TwitterUser.follows.all():
            query = Q()
            for person in _TwitterUser.follows.all():
                query = query | Q(author=person)
            tweet_list = Tweet.objects.filter(query)

        return render(request, page, {'tweet_list': tweet_list})