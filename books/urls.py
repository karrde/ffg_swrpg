from django.conf.urls import patterns, url

from books import views
from books.views import ItemListView, ItemDetailView, ItemByCategoryView, ItemCategoryDetailView
from books.views import WeaponListView, WeaponDetailView, WeaponByCategoryView, WeaponCategoryDetailView

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^items/$', ItemListView.as_view(), name='items'),
    url(r'^items_bc/$', ItemByCategoryView.as_view(), name='items_bc'),
    url(r'^items_bc/(?P<pk>\d+)/$', ItemCategoryDetailView.as_view(), name='item_category'),
    url(r'^items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),
    url(r'^weapons/$', WeaponListView.as_view(), name='weapons'),
    url(r'^weapons_bc/$', WeaponByCategoryView.as_view(), name='weapons_bc'),
    url(r'^weapons_bc/(?P<pk>\d+)/$', WeaponCategoryDetailView.as_view(), name='weapon_category'),
    url(r'^weapons/(?P<pk>\d+)/$', WeaponDetailView.as_view(), name='weapon'),
)