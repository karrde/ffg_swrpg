from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
from base.models import Index
from equipment.models import *

def sorting_context(model_class, category_model, default_sort, valid_sorts, special_sorts, request):
  order_by = request.GET.get('order_by', default_sort)
  flatened = request.GET.get('flatened', 'false')
  reverse = False
  if order_by.startswith("-"):
    order_by = order_by.lstrip("-")
    reverse = True
  if order_by not in valid_sorts:
    order_by = default_sort
  if order_by not in special_sorts:
    object_list = model_class.objects.filter(category__model=category_model).order_by(order_by, default_sort)
  elif order_by == 'index':
    object_list = [model_class.objects.get(pk=x.entry.id) for x in Index.objects.filter(entry__item__category__model=category_model)]
  elif order_by == 'crew':
    object_list = sorted(model_class.objects.filter(category__model=category_model).order_by(default_sort), key=lambda x: x.crewentry_set.aggregate(Sum('quantity')))
  if reverse:
    object_list = reversed(object_list)
  return {
    'request': request,
    'valid_sorts': valid_sorts,
    'order_by': order_by,
    '{0}_list'.format(model_class.__name__.lower()): object_list,
    'reverse': reverse,
    'flatened': flatened,
  }

class ItemListView(ListView):
  queryset = Item.objects.filter(category__model=1)
  
  def get_context_data(self, **kwargs):
    context = super(ItemListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Item, 1, 'name', ['name', 'price', 'encumbrance', 'rarity', 'index'], ['index'], self.request))
    return context 
  
class ItemCategoryView(ItemListView):
  model = Item
  template_name = 'books/item_list.html'

  def get_context_data(self, **kwargs):
    context = super(ItemCategoryView, self).get_context_data(**kwargs)
    context['item_list'] = [i for i in context['item_list'] if i.category.id == int(self.kwargs['category'])]
    return context
  
class ItemDetailView(DetailView):
  model = Item

class WeaponListView(ListView):
  model = Weapon

  def get_context_data(self, **kwargs):
    context = super(WeaponListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Weapon, 2, 'name', ['name', 'skill__name', 'damage', 'critical', 'range_band__id', 'encumbrance', 'hard_points', 'price', 'encumbrance', 'rarity', 'index'], ['index'], self.request))
    return context 
    
class WeaponCategoryView(WeaponListView):
  model = Weapon
  template_name = 'books/weapon_list.html'
  
  def get_context_data(self, **kwargs):
    context = super(WeaponCategoryView, self).get_context_data(**kwargs)
    context['weapon_list'] = [i for i in context['weapon_list'] if i.category.id == int(self.kwargs['category'])]
    return context
  
class WeaponDetailView(DetailView):
  model = Weapon

class ArmorListView(ListView):
  model = Armor

  def get_context_data(self, **kwargs):
    context = super(ArmorListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Armor, 3, 'name', ['name', 'defense', 'soak', 'price', 'encumbrance', 'hard_points', 'rarity', 'index'], ['index'], self.request))
    return context 

class ArmorDetailView(DetailView):
  model = Armor

class AttachmentListView(ListView):
  model = Attachment

  def get_context_data(self, **kwargs):
    context = super(AttachmentListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Attachment, 4, 'name', ['name', 'price', 'encumbrance', 'hard_points', 'rarity', 'index'], ['index'], self.request))
    return context 

class AttachmentCategoryView(AttachmentListView):
  model = Attachment
  template_name = 'books/attachment_list.html'

  def get_context_data(self, **kwargs):
    context = super(AttachmentCategoryView, self).get_context_data(**kwargs)
    context['attachment_list'] = [i for i in context['attachment_list'] if i.category.id == int(self.kwargs['category'])]
    return context

class AttachmentDetailView(DetailView):
  model = Attachment

class VehicleDetailView(DetailView):
  model = Vehicle
  
class VehicleListView(ListView):
  model = Vehicle

  def get_context_data(self, **kwargs):
    context = super(VehicleListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Vehicle, 5, 'name', ['name', 'silhoutte', 'speed', 'handling', 'model', 'manufacturer', 'passenger', 'price', 'encumbrance', 'hard_points', 'rarity', 'weapon_count', 'crew', 'index'], ['index', 'crew'], self.request))
    return context 

class VehicleCategoryView(VehicleListView):
  model = Vehicle
  template_name = 'books/vehicle_list.html'

  def get_context_data(self, **kwargs):
    context = super(VehicleCategoryView, self).get_context_data(**kwargs)
    context['vehicle_list'] = [i for i in context['vehicle_list'] if i.category.id == int(self.kwargs['category'])]
    return context

class StarshipDetailView(DetailView):
  model = Starship

class StarshipListView(ListView):
  model = Starship

  def get_context_data(self, **kwargs):
    context = super(StarshipListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Starship, 6, 'name', ['name', 'silhoutte', 'speed', 'handling', 'model', 'manufacturer', 'passenger', 'price', 'encumbrance', 'rarity', 'hard_points', 'weapon_count', 'crew', 'navicomputer', 'index'], ['index', 'crew'], self.request))
    return context 

class StarshipCategoryView(StarshipListView):
  model = Starship
  template_name = 'books/starship_list.html'

  def get_context_data(self, **kwargs):
    context = super(StarshipCategoryView, self).get_context_data(**kwargs)
    context['starship_list'] = [i for i in context['starship_list'] if i.category.id == int(self.kwargs['category'])]
    return context
