"""twitter_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from twitter_clone.auth.urls import url_patterns as auth_urls
from twitter_clone.TwitterUser.urls import url_patterns as TwitterUser_urls
from twitter_clone.Tweet.urls import url_patterns as Tweet_urls
from twitter_clone.Notifications.urls import url_patterns as Notification_urls

from twitter_clone.views import homepage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage')
]

urlpatterns += auth_urls
urlpatterns += TwitterUser_urls
urlpatterns += Tweet_urls
urlpatterns += Notification_urls

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)