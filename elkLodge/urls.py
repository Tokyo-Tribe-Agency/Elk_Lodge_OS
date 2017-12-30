"""elkLodge URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from lodge.views.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name='index'),
    # url(r'^login$', login, name='login'),
    # url(r'^register$', register, name='register'),
    url(r'^wedding$', wedding, name='wedding'),
    url(r'^newsletter$', newsletter, name='newsletter'),
    url(r'^new_checkout$', new_checkout, name='new_checkout'),
    url(r'^show_checkout/(?P<transaction_id>.+?)$', show_checkout, name='show_checkout'),
    url(r'^create_checkout$', create_checkout, name='create_checkout'),
    url(r'^archive$', archive, name='archive'),
    url(r'^search_keyword/$', search_keywords, name='search_keywords'),
    url(r'^event_amount$', filter_by_amount, name='filter_by_amount'),
    url(r'^recent_events$', recent_events, name='recent_events'),
    url(r'^event/(?P<event_id>.+?)$', get_this_event, name='get_this_event'),
    url(r'^add_inquiry$', add_inquiry, name='add_inquiry'),
    url(r'^success$', success, name='success'),
    url(r'^error$', error, name='error'),
    url(r'^application$', application, name='application')

    # url(r'^filter_blog_by_topic/(?P<topic_type>.+?)$', filter_blog_by_topic, name='filter_blog_by_topic'),

    # url(r'^about$', about, name='about'),
    # url(r'^events$', events, name='events'),
    # url(r'^recent_events$', recent_events, name='recent_events')

]
