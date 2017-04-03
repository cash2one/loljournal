"""lolnotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from apps.core.views import HomeView, RiotTextView

urlpatterns = [
    url('^summoner/', include('django.contrib.auth.urls')),
    url('^summoner/', include('apps.summoner.urls')),
    url('^faq/', include('apps.faq.urls')),
    url('^match/', include('apps.match.urls')),

    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^riot\.txt$', RiotTextView.as_view(), name='riot.txt'),
    url(r'^admin/', admin.site.urls),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
