from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import RedirectView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ffg_swrpg.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'ffg_swrpg.views.index_view', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^equipment/', include('equipment.urls', namespace='equipment')),
    url(r'^books/', include('books.urls', namespace='books')),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
