from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.Tweet.models import Tweet
from twitter_clone.Tweet.forms import NewTweetForm

@login_required
def homepage(request, *args, **kwargs):
    page = 'timeline.html'
    if request.method == 'GET':
        u = request.user
        form = NewTweetForm()
        button_label = 'Submit'
        _TwitterUser = TwitterUser.objects.get(user=u)
        tweet_list = []
        query = Q()
        query = query | Q(author=_TwitterUser)
        if _TwitterUser.following.all():
            for person in _TwitterUser.following.all():
                query = query | Q(author=person)
        tweet_list = Tweet.objects.filter(query).order_by('-created_at')
        
        return render(request, page, {'form': form, 'tweet_list': tweet_list, 'button_label': button_label})