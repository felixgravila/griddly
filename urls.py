from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', 'common.views.base'),
    url(r'^user/login/', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/?$',  'django.contrib.auth.views.logout_then_login'),
    url(r'^user/register/$',  'account.views.register'),
    url(r'^game/?$',  'game.views.start'),
    url(r'^external-api/login/$',  'external-api.views.login'),
    url(r'^external-api/checkin/$',  'external-api.views.checkingin'),
)

urlpatterns += staticfiles_urlpatterns()