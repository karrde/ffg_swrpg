from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
from base.models import Index
from base.views import sorting_context
from character.models import *

class SkillListView(ListView):
  model = Skill
  
  def get_context_data(self, **kwargs):
    context = super(SkillListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Skill, 'name', ['name', 'characteristic', 'skill_type', 'index'], ['index'], self.request))
    return context 
  
  
class SkillDetailView(DetailView):
  model = Skill


class TalentListView(ListView):
  model = Talent

  def get_context_data(self, **kwargs):
    context = super(TalentListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Talent, 'name', ['name', 'activation', 'ranked', 'force_sensitive', 'index'], ['index'], self.request))
    return context 


class TalentDetailView(DetailView):
  model = Talent

class AbilityListView(ListView):
  model = Ability

  def get_context_data(self, **kwargs):
    context = super(AbilityListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Ability, 'name', ['name', 'description', 'index'], ['index'], self.request))
    return context 


class AbilityDetailView(DetailView):
  model = Ability

class SpeciesDetailView(DetailView):
  model = Species
