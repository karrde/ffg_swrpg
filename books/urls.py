from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from books.views import *

urlpatterns = patterns('',
    url(r'^$', BookListView.as_view(), name='index'),
    url(r'^book/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book'),
    url(r'^items/$', RedirectView.as_view(url='/equipment/gear/')),
    url(r'^items/category/(?P<category>\d+)/$', RedirectView.as_view(url='/equipment/gear/category/%(category)s/')),
    url(r'^items/(?P<pk>\d+)/$', RedirectView.as_view(url='/equipment/gear/%(pk)s/')),
    url(r'^weapons/$', RedirectView.as_view(url='/equipment/weapons/')),
    url(r'^weapons/category/(?P<category>\d+)/$', RedirectView.as_view(url='/equipment/weapons/category/%(category)s/')),
    url(r'^weapons/(?P<pk>\d+)/$', RedirectView.as_view(url='/equipment/weapons/%(pk)s/')),
    url(r'^armor/$', RedirectView.as_view(url='/equipment/armor/')),
    url(r'^armor/(?P<pk>\d+)/$', RedirectView.as_view(url='/equipment/armor/%(pk)s/')),
    url(r'^attachments/$', RedirectView.as_view(url='/equipment/attachments/')),
    url(r'^attachments/category/(?P<category>\d+)/$', RedirectView.as_view(url='/equipment/attachment/category/%(category)s/')),
    url(r'^attachments/(?P<pk>\d+)/$', RedirectView.as_view(url='/equipment/attachments/%(pk)s/')),
    url(r'^vehicles/$', RedirectView.as_view(url='/transportation/vehicles/')),
    url(r'^vehicles/(?P<pk>\d+)/$', RedirectView.as_view(url='/transportation/vehicles/%(pk)s')),
    url(r'^vehicles/category/(?P<category>\d+)/$', RedirectView.as_view(url='/transportation/vehicles/category/%(category)s')),
    url(r'^starships/$', RedirectView.as_view(url='/transportation/starships/')),
    url(r'^starships/(?P<pk>\d+)/$', RedirectView.as_view(url='/transportation/starships/%(pk)s')),
    url(r'^starshipscategory/(?P<category>\d+)/$', RedirectView.as_view(url='/transportation/starships/category/%(category)s')),
)