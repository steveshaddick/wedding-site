from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'wedding_rsvp.views.form', name='form'),
    url(r'^rsvp/', include('wedding_rsvp.urls', namespace='wedding_rsvp')),

)