from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView
from ffg_swrpg.feeds import *
from ffg_swrpg.views import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'ffg_swrpg.views.index_view', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^equipment/', include('equipment.urls', namespace='equipment')),
    url(r'^transportation/', include('transportation.urls', namespace='transportation')),
    url(r'^adversaries/', include('adversaries.urls', namespace='adversaries')),
    url(r'^character/', include('character.urls', namespace='character')),
    url(r'^books/', include('books.urls', namespace='books')),
    url(r'^base/', include('base.urls', namespace='base')),
    url(r'^blog/(?P<pk>\d+)/$', BlogDetailView.as_view(), name='blog'),
    url(r'^entries/feed/$', EntryFeed()),
    url(r'^blog/feed/$', BlogFeed()),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
