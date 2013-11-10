from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^submit/$', 'wedding_rsvp.views.submit', name='submit'),

)