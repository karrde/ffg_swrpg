from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from transportation.views import *

urlpatterns = patterns('',
    url(r'^$', CategoryListView.as_view(), name='index'),
    url(r'^vehicles/$', VehicleListView.as_view(), name='vehicles'),
    url(r'^vehicles/(?P<pk>\d+)/$', VehicleDetailView.as_view(), name='vehicle'),
    url(r'^vehicles/category/(?P<category>\d+)/$', VehicleCategoryView.as_view(), name='vehicle_category'),
    url(r'^starships/$', StarshipListView.as_view(), name='starships'),
    url(r'^starships/(?P<pk>\d+)/$', StarshipDetailView.as_view(), name='starship'),
    url(r'^starships/category/(?P<category>\d+)/$', StarshipCategoryView.as_view(), name='starship_category'),
    url(r'^vehicleattachments/$', VehicleAttachmentListView.as_view(), name='vehicleattachments'),
    url(r'^vehicleattachments/category/(?P<category>\d+)/$', VehicleAttachmentCategoryView.as_view(), name='vehicleattachment_category'),
    url(r'^vehicleattachments/(?P<pk>\d+)/$', VehicleAttachmentDetailView.as_view(), name='vehicleattachment'),
)