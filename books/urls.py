from django.conf.urls import patterns, url

from books import views
from books.views import ItemListView, ItemDetailView, ItemByCategoryView, ItemCategoryDetailView
from books.views import WeaponListView, WeaponDetailView, WeaponByCategoryView, WeaponCategoryDetailView, BookListView, BookDetailView, ArmorListView, ArmorDetailView, AttachmentListView, AttachmentByCategoryView, AttachmentCategoryDetailView, AttachmentDetailView

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
)