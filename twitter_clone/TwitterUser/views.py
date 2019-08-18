from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

from twitter_clone.TwitterUser.forms import EditHeadlineForm

from twitter_clone.Tweet.models import Tweet
from twitter_clone.TwitterUser.models import TwitterUser
from twitter_clone.Notifications.views import get_notifications

def user_profile(request, *args, **kwargs):
    if request.method == 'GET':
        page = 'profile.html'
        name = request.GET.get('username')
        u = None
        try:
            u = User.objects.get(username=name)
        except Exception as e:
            pass
        if u:
            visitor_u = request.user
            is_following = False
            _TwitterUser = TwitterUser.objects.get(user=u)
            tweet_list = Tweet.objects.all().filter(author=_TwitterUser).order_by('-created_at')
            if str(visitor_u) == 'AnonymousUser':
                is_following = None
                not_logged_in = True
                return render(request, page, {'not_logged_in': not_logged_in,'user': None, 'notifications': None, 'TwitterUser': _TwitterUser, 'tweet_list': tweet_list, 'is_following': is_following})
            elif visitor_u.username == _TwitterUser.user.username:
                is_following = None
                headline = _TwitterUser.headline
                form = EditHeadlineForm(initial={'headline': headline})
                return render(request, page, {'form': form, 'user': visitor_u, 'TwitterUser': _TwitterUser, 'tweet_list': tweet_list, 'is_following': is_following})
            else:
                visitor = TwitterUser.objects.get(user=visitor_u)
                _TwitterUser = TwitterUser.objects.get(user=u)
                if _TwitterUser in visitor.following.all():
                    is_following = True
                return render(request, page, {'user': visitor_u, 'TwitterUser': _TwitterUser, 'tweet_list': tweet_list, 'is_following': is_following})    
        else:
            headline = request.GET.get('headline')
            u = request.user
            _TwitterUser = TwitterUser.objects.get(user=u)
            if headline:
                _TwitterUser.headline = headline
                _TwitterUser.save()
            is_following = None
            tweet_list = Tweet.objects.all().filter(author=_TwitterUser).order_by('-created_at')
            form = EditHeadlineForm(initial={'headline': headline})

            message = 'Headline saved!'

            return render(request, page, {'message':message, 'form': form, 'user': u, 'TwitterUser': _TwitterUser, 'tweet_list': tweet_list, 'is_following': is_following})

            

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

def find(request, *args, **kwargs):
    if request.method == 'GET':
        page = 'find_users.html'
        u = None
        logged_in_user = None
        _TwitterUser = None
        _Notifications = None
        if not request.user.is_anonymous:      
            u = request.user  
            logged_in_user = TwitterUser.objects.get(user=u)
            _TwitterUser = TwitterUser.objects.get(user=u)
            _Notifications = get_notifications(_TwitterUser)
        user_list = TwitterUser.objects.all().order_by('user__username')

        return render(request, page, {'user': u, 'logged_in_user': logged_in_user, 'notifications': _Notifications, 'user_list': user_list})


