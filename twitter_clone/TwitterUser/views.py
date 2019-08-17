from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from twitter_clone.Tweet.models import Tweet
from twitter_clone.TwitterUser.models import TwitterUser

def user_profile(request, *args, **kwargs):
    if request.method == 'GET':
        name = request.GET.get('username')
        u = None
        try:
            u = User.objects.get(username=name)
        except Exception as e:
            pass
        if u:
            visitor_u = request.user
            is_following = False
            page = 'profile.html'
            _TwitterUser = TwitterUser.objects.get(user=u)
            tweet_list = Tweet.objects.all().filter(author=_TwitterUser).order_by('-created_at')
            if str(visitor_u) == 'AnonymousUser' or visitor_u.username == _TwitterUser.user.username:
                is_following = None
                return render(request, page, {'TwitterUser': _TwitterUser, 'tweet_list': tweet_list, 'is_following': is_following})
            else:
                visitor = TwitterUser.objects.get(user=visitor_u)
                _TwitterUser = TwitterUser.objects.get(user=u)
                if _TwitterUser in visitor.following.all():
                    is_following = True
                return render(request, page, {'TwitterUser': _TwitterUser, 'tweet_list': tweet_list, 'is_following': is_following})    
        else:
            return HttpResponseRedirect(reverse('homepage'))

@login_required
def follow(request, *args, **kwargs):
    if request.method == 'GET':
        _TwitterUser = request.user.twitteruser
        name = request.GET.get('username')
        u=User.objects.get(username=name)
        user_to_follow = TwitterUser.objects.get(user=u)

        if user_to_follow not in _TwitterUser.following.all():
            _TwitterUser.following.add(user_to_follow)
            user_to_follow.followers.add(_TwitterUser)
        return HttpResponseRedirect(f'/profile/?username={user_to_follow.user.username}')
    else:
        return HttpResponseRedirect(reverse('homepage'))

@login_required
def unfollow(request, *args, **kwargs):
    if request.method == 'GET':
        _TwitterUser = request.user.twitteruser
        name = request.GET.get('username')
        u=User.objects.get(username=name)
        user_to_unfollow = TwitterUser.objects.get(user=u)

        if user_to_unfollow in _TwitterUser.following.all():
            _TwitterUser.following.remove(user_to_unfollow)
            user_to_unfollow.followers.remove(_TwitterUser)
        return HttpResponseRedirect(f'/profile/?username={user_to_unfollow.user.username}')
    else:
        return HttpResponseRedirect(reverse('homepage'))
