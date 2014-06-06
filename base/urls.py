from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from base.views import *

urlpatterns = patterns('',
    url(r'^book/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book'),
)