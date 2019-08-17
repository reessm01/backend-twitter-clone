from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
import re

from twitter_clone.Tweet.forms import NewTweetForm

from twitter_clone.Tweet.models import Tweet
from twitter_clone.TwitterUser.models import TwitterUser

@login_required
def tweet(request, *args, **kwargs):
    if request.method == 'POST':
        form = NewTweetForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = request.user
            if u is not None:
                Tweet.objects.create(
                text=data['text'],
                author=TwitterUser.objects.get(user=u)
                )
            else:
                page = 'timeline.html'
                tweet_error_message = 'Oops something went wrong!'
                form = NewTweetForm()
                return render(request, page, {'form': form, 'tweet_error_message': tweet_error_message})

            return HttpResponseRedirect(reverse('homepage'))
    elif request.method == 'GET':
        id = request.GET.get('id')
        tweet = Tweet.objects.get(id=id)
        page = 'single_tweet.html'

        return render(request, page, {'tweet': tweet})

def mentions_checker(text):
    pattern = re.compile(r'@([A-Za-z0-9_]+[A-Za-z0-9_]+)')
    print(re.search(pattern, text).group())