from django.shortcuts import render
from django.views.generic import ListView, DetailView

from transportation.models import *
from equipment.views import sorting_context

class VehicleDetailView(DetailView):
  model = Vehicle
  
class VehicleListView(ListView):
  model = Vehicle

  def get_context_data(self, **kwargs):
    context = super(VehicleListView, self).get_context_data(**kwargs)
    context.update(sorting_context(self.model, 'name', ['name', 'silhoutte', 'speed', 'handling', 'model', 'manufacturer', 'passenger', 'equipment__price', 'encumbrance', 'hard_points', 'equipment__rarity', 'weapon_count', 'crew', 'index'], ['index', 'crew'], self.request))
    return context 

class VehicleCategoryView(VehicleListView):
  model = Vehicle
  template_name = 'transportation/vehicle_list.html'

  def get_context_data(self, **kwargs):
    context = super(VehicleCategoryView, self).get_context_data(**kwargs)
    context['vehicle_list'] = [i for i in context['vehicle_list'] if i.equipment.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
    return context

class StarshipDetailView(DetailView):
  model = Starship

def sorting_context2(view):
  # This was a long dark rabbit hole. But there's a good idea here, come back to it.
  order_by = view.request.GET.get('order_by', view.model._meta.ordering[0])
  flattened = view.request.GET.get('flattened', 'false')
  reverse = False
  if order_by.startswith("-"):
    order_by = order_by.lstrip("-")
    reverse = True
  if order_by not in view.valid_sorts:
    order_by = view.model._meta.ordering[0]
  if order_by not in view.special_sorts:
    object_list = view.model.objects.order_by(order_by, view.model._meta.ordering[0])
  elif order_by == 'index':
    object_list = [view.model.objects.get(pk=x.entry.id) for x in Index.objects.filter(entry__model=model_class.__name__)]
  elif order_by == 'crew':
    object_list = sorted(view.model.objects.all(), key=lambda x: x.crewentry_set.aggregate(Sum('quantity')))
  if reverse:
    object_list = reversed(object_list)
  return {
    'request': view.request,
    'valid_sorts': view.valid_sorts,
    'special_sorts': view.special_sorts,
    'order_by': order_by,
    '{0}_list'.format(view.model.__name__.lower()): object_list,
    'reverse': reverse,
    'flattened': flattened,
    'in_category': "category" in view.request.path,
  }



class StarshipListView(ListView):
  model = Starship
  valid_sorts = ['name', 'silhoutte', 'speed', 'handling', 'model', 'manufacturer', 'passenger', 'equipment__price', 'encumbrance', 'equipment__rarity', 'hard_points', 'weapon_count', 'crew', 'navicomputer', 'index']
  special_sorts = ['index', 'crew']

  def get_context_data(self, **kwargs):
    context = super(StarshipListView, self).get_context_data(**kwargs)
    context.update(sorting_context(self.model, 'name', ['name', 'silhoutte', 'speed', 'handling', 'model', 'manufacturer', 'passenger', 'equipment__price', 'encumbrance', 'equipment__rarity', 'hard_points', 'weapon_count', 'crew', 'navicomputer', 'index'], ['index', 'crew'], self.request))
    return context 


class StarshipCategoryView(StarshipListView):
  model = Starship
  template_name = 'transportation/starship_list.html'

  def get_context_data(self, **kwargs):
    context = super(StarshipCategoryView, self).get_context_data(**kwargs)
#    if context['order_by'] not in context['special_sorts']:
#      context['starship_list'] = context['starship_list'].filter(category__id=int(self.kwargs['category']))
#    else:
    context['starship_list'] = [i for i in context['starship_list'] if i.equipment.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
    return context


class VehicleAttachmentListView(ListView):
  model = VehicleAttachment
  
  def get_context_data(self, **kwargs):
    context = super(VehicleAttachmentListView, self).get_context_data(**kwargs)
    context.update(sorting_context(self.model, 'name', ['name', 'equipment__price', 'hard_points', 'equipment__rarity', 'index'], ['index'], self.request))
    return context 

class VehicleAttachmentCategoryView(VehicleAttachmentListView):
  model = VehicleAttachment
  template_name = 'transportation/vehicleattachment_list.html'

  def get_context_data(self, **kwargs):
    context = super(VehicleAttachmentCategoryView, self).get_context_data(**kwargs)
    context['vehicleattachment_list'] = [i for i in context['vehicleattachment_list'] if i.equipment.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
    return context

class VehicleAttachmentDetailView(DetailView):
  model = VehicleAttachment

class CategoryListView(ListView):
  queryset = Category.objects.filter(model__in=Category.model_numbers()).order_by('model', 'name')
