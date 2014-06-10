from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from adversaries.views import *

urlpatterns = patterns('',
    url(r'^$', AdversaryListView.as_view(), name='index'),
#    url(r'^adversaries/$', GearListView.as_view()),
#    url(r'^adversaries/category/(?P<category>\d+)/$', GearCategoryView.as_view()),
    url(r'^adversary/(?P<pk>\d+)/$', AdversaryDetailView.as_view()),
)