from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from adversaries.views import *

urlpatterns = patterns('',
    url(r'^$', AdversaryListView.as_view(), name='index'),
    url(r'^adversaries/$', AdversaryListView.as_view(), name='adversaries'),
    url(r'^adversaries/(?P<level>\w+)/$', AdversaryLevelView.as_view(), name='adversary_level'),
    url(r'^adversary/(?P<pk>\d+)/$', AdversaryDetailView.as_view(), name='adversary'),
)