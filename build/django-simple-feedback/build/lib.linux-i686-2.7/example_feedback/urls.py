from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url('^$', direct_to_template, {'template': 'base.html'}),

    url('^feedback/$', include('feedback.urls')),

    (r'^accounts/login/$', 'django.contrib.auth.views.login'),
    # Examples:
    # url(r'^$', 'example_feedback.views.home', name='home'),
    # url(r'^example_feedback/', include('example_feedback.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
