from django.conf.urls.defaults import *
from django.conf import settings
import django.views.static

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL.lstrip('/'),
        django.views.static.serve, {'document_root': settings.MEDIA_ROOT}),

    # Server only sertain directories from data directory
    url(r'^(data/photos/.*)$',
        django.views.static.serve, {'document_root': settings.ROOT}),
    url(r'^(data/us/112/stats/person/sponsorshipanalysis/.*)$',
        django.views.static.serve, {'document_root': settings.ROOT}),
    url(r'', include('redirect.urls')),
    url(r'', include('website.urls')),
    url(r'^person/', include('person.urls')),
    url(r'', include('committee.urls')),
    url(r'', include('vote.urls')),
)