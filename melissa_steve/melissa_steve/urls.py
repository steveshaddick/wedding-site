from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'melissa_steve.views.home', name='home'),
    url(r'^rsvp/', include('wedding_rsvp.urls', namespace='wedding_rsvp')),

    url(r'^admin/', include(admin.site.urls)),
)
