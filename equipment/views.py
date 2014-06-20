from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
from base.models import Index
from equipment.models import *

def sorting_context(model_class, default_sort, valid_sorts, special_sorts, request):
  order_by = request.GET.get('order_by', default_sort)
  flattened = request.GET.get('flattened', 'false')
  reverse = False
  if order_by.startswith("-"):
    order_by = order_by.lstrip("-")
    reverse = True
  if order_by not in valid_sorts:
    order_by = default_sort
  if order_by not in special_sorts:
    object_list = model_class.objects.filter(equipment__isnull=False).filter(model=model_class.__name__).order_by(order_by, default_sort)
  elif order_by == 'index':
    object_list = [x for x in [model_class.objects.get(pk=x.entry.id) for x in Index.objects.filter(entry__model=model_class.__name__)] if hasattr(x, 'equipment')]
  elif order_by == 'crew':
    object_list = sorted(model_class.objects.all(), key=lambda x: x.crewentry_set.aggregate(Sum('quantity')))
  if reverse:
    object_list = reversed(object_list)
  return {
    'request': request,
    'valid_sorts': valid_sorts,
    'special_sorts': special_sorts,
    'order_by': order_by,
    '{0}_list'.format(model_class.__name__.lower()): object_list,
    'reverse': reverse,
    'flattened': flattened,
    'in_category': "category" in request.path,
  }

class GearListView(ListView):
  queryset = Gear.objects.filter(equipment__isnull=False)
  
  def get_context_data(self, **kwargs):
    context = super(GearListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Gear, 'name', ['name', 'equipment__price', 'encumbrance', 'equipment__rarity', 'index'], ['index'], self.request))
    return context 
  
class GearCategoryView(GearListView):
  model = Gear
  template_name = 'equipment/gear_list.html'

  def get_context_data(self, **kwargs):
    context = super(GearCategoryView, self).get_context_data(**kwargs)
    context['gear_list'] = [i for i in context['gear_list'] if i.equipment.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
    return context
  
class GearDetailView(DetailView):
  model = Gear

class WeaponListView(ListView):
  model = Weapon

  def get_context_data(self, **kwargs):
    context = super(WeaponListView, self).get_context_data(**kwargs)
    context.update(sorting_context(self.model, 'name', ['name', 'weapon_skill', 'damage', 'critical', 'weapon_range', 'encumbrance', 'hard_points', 'equipment__price', 'encumbrance', 'equipment__rarity', 'index'], ['index'], self.request))
    return context 
    
class WeaponCategoryView(WeaponListView):
  model = Weapon
  template_name = 'equipment/weapon_list.html'
  
  def get_context_data(self, **kwargs):
    context = super(WeaponCategoryView, self).get_context_data(**kwargs)
    context['weapon_list'] = [i for i in context['weapon_list'] if i.equipment.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
    return context
  
class WeaponDetailView(DetailView):
  model = Weapon

class ArmorListView(ListView):
  model = Armor

  def get_context_data(self, **kwargs):
    context = super(ArmorListView, self).get_context_data(**kwargs)
    context.update(sorting_context(self.model, 'name', ['name', 'defense', 'soak', 'equipment__price', 'encumbrance', 'hard_points', 'equipment__rarity', 'index'], ['index'], self.request))
    return context 

class ArmorDetailView(DetailView):
  model = Armor

class AttachmentListView(ListView):
  model = Attachment

  def get_context_data(self, **kwargs):
    context = super(AttachmentListView, self).get_context_data(**kwargs)
    context.update(sorting_context(self.model, 'name', ['name', 'price', 'encumbrance', 'hard_points', 'rarity', 'index'], ['index'], self.request))
    return context 

class AttachmentCategoryView(AttachmentListView):
  model = Attachment
  template_name = 'equipment/attachment_list.html'

  def get_context_data(self, **kwargs):
    context = super(AttachmentCategoryView, self).get_context_data(**kwargs)
    context['attachment_list'] = [i for i in context['attachment_list'] if i.equipment.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
    return context

class AttachmentDetailView(DetailView):
  model = Attachment

class CategoryListView(ListView):
  queryset = Category.objects.filter(model__in=Category.model_numbers()).order_by('model', 'name')

