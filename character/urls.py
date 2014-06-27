from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
from django.views.generic import TemplateView


from character.views import *

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="character/index.html"), name='index'),
    url(r'^skill/$', SkillListView.as_view(), name='skills'),
    url(r'^skill/(?P<pk>\d+)/$', SkillDetailView.as_view(), name='skill'),
    url(r'^talent/$', TalentListView.as_view(), name='talents'),
    url(r'^talent/(?P<pk>\d+)/$', TalentDetailView.as_view(), name='talent'),
    url(r'^ability/$', AbilityListView.as_view(), name='abilities'),
    url(r'^ability/(?P<pk>\d+)/$', AbilityDetailView.as_view(), name='ability'),
    url(r'^species/(?P<pk>\d+)/$', SpeciesDetailView.as_view(), name='species'),
)