from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
from base.models import Index
from base.views import sorting_context
from equipment.views import sorting_context as equipment_sorting_context
from adversaries.models import *

class AdversaryDetailView(DetailView):
  model = Adversary

class AdversaryListView(ListView):
  model = Adversary
  
  def get_context_data(self, **kwargs):
    context = super(AdversaryListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Adversary, 'name', ['name', 'level', 'index'], ['index'], self.request))
    return context 
  
class CreatureWeaponDetailView(DetailView):
  model = CreatureWeapon
  template_name = "equipment/weapon_detail.html"
  
  def get_context_data(self, **kwargs):
    context = super(CreatureWeaponDetailView, self).get_context_data(**kwargs)
    context['weapon'] = self.get_object()
    return context
    
class CreatureWeaponListView(ListView):
  model = CreatureWeapon

  def get_context_data(self, **kwargs):
    context = super(CreatureWeaponListView, self).get_context_data(**kwargs)
    context.update(sorting_context(CreatureWeapon, 'name', ['name', 'weapon_skill', 'damage', 'critical', 'weapon_range', 'index'], ['index'], self.request))
    return context 

class CreatureDetailView(DetailView):
  model = Creature
  template_name = 'adversaries/adversary_detail.html'
  
  def get_context_data(self, **kwargs):
    context = super(CreatureDetailView, self).get_context_data(**kwargs)
    context['adversary'] = self.get_object()
    return context

class CreatureListView(ListView):
  model = Creature

  def get_context_data(self, **kwargs):
    context = super(CreatureListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Creature, 'name', ['name', 'level', 'index'], ['index'], self.request))
    return context 

class WeaponListView(ListView):
  model = equipment.models.Weapon
  template_name = 'adversaries/weapon_list.html'

  def get_context_data(self, **kwargs):
    context = super(WeaponListView, self).get_context_data(**kwargs)
    context.update(equipment_sorting_context(equipment.models.Weapon, 'name', ['name', 'weapon_skill', 'damage', 'critical', 'weapon_range', 'index'], ['index'], self.request, True))
    return context 

class GearListView(ListView):
  model = equipment.models.Gear
  template_name = 'adversaries/gear_list.html'

  def get_context_data(self, **kwargs):
    context = super(GearListView, self).get_context_data(**kwargs)
    context.update(equipment_sorting_context(self.model, 'name', ['name', 'encumbrance', 'index'], ['index'], self.request, True))
    return context 

class ArmorListView(ListView):
  model = equipment.models.Armor
  template_name = 'adversaries/armor_list.html'

  def get_context_data(self, **kwargs):
    context = super(ArmorListView, self).get_context_data(**kwargs)
    context.update(equipment_sorting_context(self.model, 'name', ['name', 'defense', 'soak', 'encumbrance', 'hard_points', 'index'], ['index'], self.request, True))
    return context 
  
  
  