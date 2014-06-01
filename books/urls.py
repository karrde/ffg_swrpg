from django.conf.urls import patterns, url

from books import views
from books.views import ItemListView, ItemDetailView, ItemByCategoryView, ItemCategoryDetailView
from books.views import WeaponListView, WeaponDetailView, WeaponByCategoryView, WeaponCategoryDetailView, BookListView, BookDetailView, ArmorListView, ArmorDetailView, AttachmentListView, AttachmentByCategoryView, AttachmentCategoryDetailView, AttachmentDetailView, VehicleDetailView, VehicleListView, VehicleByCategoryView, VehicleCategoryDetailView, StarshipDetailView, StarshipListView, StarshipByCategoryView, StarshipCategoryDetailView

urlpatterns = patterns('',
    url(r'^$', BookListView.as_view(), name='index'),
    url(r'^book/(?P<pk>\d+)/$', BookDetailView.as_view(), name='book'),
    url(r'^items/$', ItemListView.as_view(), name='items'),
    url(r'^items_bc/$', ItemByCategoryView.as_view(), name='items_bc'),
    url(r'^items_bc/(?P<pk>\d+)/$', ItemCategoryDetailView.as_view(), name='item_category'),
    url(r'^items/(?P<pk>\d+)/$', ItemDetailView.as_view(), name='item'),
    url(r'^weapons/$', WeaponListView.as_view(), name='weapons'),
    url(r'^weapons_bc/$', WeaponByCategoryView.as_view(), name='weapons_bc'),
    url(r'^weapons_bc/(?P<pk>\d+)/$', WeaponCategoryDetailView.as_view(), name='weapon_category'),
    url(r'^weapons/(?P<pk>\d+)/$', WeaponDetailView.as_view(), name='weapon'),
    url(r'^armor/$', ArmorListView.as_view(), name='armors'),
    url(r'^armor/(?P<pk>\d+)/$', ArmorDetailView.as_view(), name='armor'),
    url(r'^attachments/$', AttachmentListView.as_view(), name='attachments'),
    url(r'^attachments_bc/$', AttachmentByCategoryView.as_view(), name='attachments_bc'),
    url(r'^attachments_bc/(?P<pk>\d+)/$', AttachmentCategoryDetailView.as_view(), name='attachment_category'),
    url(r'^attachments/(?P<pk>\d+)/$', AttachmentDetailView.as_view(), name='attachment'),
    url(r'^vehicles/$', VehicleListView.as_view(), name='vehicles'),
    url(r'^vehicles/(?P<pk>\d+)/$', VehicleDetailView.as_view(), name='vehicle'),
    url(r'^vehicles_bc/$', VehicleByCategoryView.as_view(), name='vehicles_bc'),
    url(r'^vehicles_bc/(?P<pk>\d+)/$', VehicleCategoryDetailView.as_view(), name='vehicle_category'),
    url(r'^starships/$', StarshipListView.as_view(), name='starships'),
    url(r'^starships/(?P<pk>\d+)/$', StarshipDetailView.as_view(), name='starship'),
    url(r'^starships_bc/$', StarshipByCategoryView.as_view(), name='starships_bc'),
    url(r'^starships_bc/(?P<pk>\d+)/$', StarshipCategoryDetailView.as_view(), name='starship_category'),
)