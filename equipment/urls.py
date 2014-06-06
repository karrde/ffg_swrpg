from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from equipment.views import *

urlpatterns = patterns('',
    url(r'^$', ItemListView.as_view(), name='index'),
    url(r'^items/$', ItemListView.as_view()),
    url(r'^items/category/(?P<category>\d+)/$', ItemCategoryView.as_view()),
    url(r'^items/(?P<pk>\d+)/$', ItemDetailView.as_view()),
    url(r'^gear/$', ItemListView.as_view(), name='gears'),
    url(r'^gear/category/(?P<category>\d+)/$', ItemCategoryView.as_view(), name='gear_category'),
    url(r'^gear/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='gear'),
    url(r'^weapons/$', WeaponListView.as_view(), name='weapons'),
    url(r'^weapons/category/(?P<category>\d+)/$', WeaponCategoryView.as_view(), name='weapon_category'),
    url(r'^weapons/(?P<pk>\d+)/$', WeaponDetailView.as_view(), name='weapon'),
    url(r'^armor/$', ArmorListView.as_view(), name='armors'),
    url(r'^armor/(?P<pk>\d+)/$', ArmorDetailView.as_view(), name='armor'),
    url(r'^attachments/$', AttachmentListView.as_view(), name='attachments'),
    url(r'^attachments/category/(?P<category>\d+)/$', AttachmentCategoryView.as_view(), name='attachment_category'),
    url(r'^attachments/(?P<pk>\d+)/$', AttachmentDetailView.as_view(), name='attachment'),
    url(r'^vehicles/$', VehicleListView.as_view(), name='vehicles'),
    url(r'^vehicles/(?P<pk>\d+)/$', VehicleDetailView.as_view(), name='vehicle'),
    url(r'^vehicles/category/(?P<category>\d+)/$', VehicleCategoryView.as_view(), name='vehicle_category'),
    url(r'^starships/$', StarshipListView.as_view(), name='starships'),
    url(r'^starships/(?P<pk>\d+)/$', StarshipDetailView.as_view(), name='starship'),
    url(r'^starshipscategory/(?P<category>\d+)/$', StarshipCategoryView.as_view(), name='starship_category'),
)