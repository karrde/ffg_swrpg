from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView

from adversaries.views import *

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="adversaries/index.html"), name='index'),
    url(r'^$', AdversaryListView.as_view(), name='index'),
    url(r'^adversaries/$', AdversaryListView.as_view(), name='adversaries'),
    url(r'^adversary/(?P<pk>\d+)/$', AdversaryDetailView.as_view(), name='adversary'),
    url(r'^gear/$', GearListView.as_view(), name='gear'),
    url(r'^weapons/$', WeaponListView.as_view(), name='weapons'),
    url(r'^armor/$', ArmorListView.as_view(), name='armor'),
    url(r'^creatureweapon/(?P<pk>\d+)/$', CreatureWeaponDetailView.as_view(), name='creatureweapon'),
    url(r'^creatureweapons/$', CreatureWeaponListView.as_view(), name='creatureweapons'),
    url(r'^creatures/$', CreatureListView.as_view(), name='creatures'),
    url(r'^creature/(?P<pk>\d+)/$', CreatureDetailView.as_view(), name='creature'),
)