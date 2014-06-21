from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from adversaries.views import *

urlpatterns = patterns('',
    url(r'^$', AdversaryListView.as_view(), name='index'),
    url(r'^adversaries/$', AdversaryListView.as_view(), name='adversaries'),
    url(r'^adversary/(?P<pk>\d+)/$', AdversaryDetailView.as_view(), name='adversary'),
    url(r'^creatureweapon/(?P<pk>\d+)/$', CreatureWeaponDetailView.as_view(), name='creatureweapon'),
    url(r'^creatureweapons/$', CreatureWeaponListView.as_view(), name='creatureweapons'),
    url(r'^creatures/$', CreatureListView.as_view(), name='creatures'),
    url(r'^creature/(?P<pk>\d+)/$', CreatureDetailView.as_view(), name='creature'),
)