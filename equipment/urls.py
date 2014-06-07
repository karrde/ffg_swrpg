from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView

from equipment.views import *

urlpatterns = patterns('',
    url(r'^$', GearListView.as_view(), name='index'),
    url(r'^items/$', GearListView.as_view()),
    url(r'^items/category/(?P<category>\d+)/$', GearCategoryView.as_view()),
    url(r'^items/(?P<pk>\d+)/$', GearDetailView.as_view()),
    url(r'^gear/$', GearListView.as_view(), name='gears'),
    url(r'^gear/category/(?P<category>\d+)/$', GearCategoryView.as_view(), name='gear_category'),
    url(r'^gear/(?P<pk>\d+)/$', GearDetailView.as_view(), name='gear'),
    url(r'^weapons/$', WeaponListView.as_view(), name='weapons'),
    url(r'^weapons/category/(?P<category>\d+)/$', WeaponCategoryView.as_view(), name='weapon_category'),
    url(r'^weapons/(?P<pk>\d+)/$', WeaponDetailView.as_view(), name='weapon'),
    url(r'^armor/$', ArmorListView.as_view(), name='armors'),
    url(r'^armor/(?P<pk>\d+)/$', ArmorDetailView.as_view(), name='armor'),
    url(r'^attachments/$', AttachmentListView.as_view(), name='attachments'),
    url(r'^attachments/category/(?P<category>\d+)/$', AttachmentCategoryView.as_view(), name='attachment_category'),
    url(r'^attachments/(?P<pk>\d+)/$', AttachmentDetailView.as_view(), name='attachment'),
)