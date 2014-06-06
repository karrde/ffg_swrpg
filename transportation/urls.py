from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from transportation.views import *

urlpatterns = patterns('',
    url(r'^$', VehicleListView.as_view(), name='index'),
    url(r'^vehicles/$', VehicleListView.as_view(), name='vehicles'),
    url(r'^vehicles/(?P<pk>\d+)/$', VehicleDetailView.as_view(), name='vehicle'),
    url(r'^vehicles/category/(?P<category>\d+)/$', VehicleCategoryView.as_view(), name='vehicle_category'),
    url(r'^starships/$', StarshipListView.as_view(), name='starships'),
    url(r'^starships/(?P<pk>\d+)/$', StarshipDetailView.as_view(), name='starship'),
    url(r'^starshipscategory/(?P<category>\d+)/$', StarshipCategoryView.as_view(), name='starship_category'),
)