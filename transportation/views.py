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
    context.update(sorting_context(Vehicle, 5, 'name', ['name', 'silhoutte', 'speed', 'handling', 'model', 'manufacturer', 'passenger', 'price', 'encumbrance', 'hard_points', 'rarity', 'weapon_count', 'crew', 'index'], ['index', 'crew'], self.request))
    return context 

class VehicleCategoryView(VehicleListView):
  model = Vehicle
  template_name = 'transportation/vehicle_list.html'

  def get_context_data(self, **kwargs):
    context = super(VehicleCategoryView, self).get_context_data(**kwargs)
    context['vehicle_list'] = [i for i in context['vehicle_list'] if i.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
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
  template_name = 'transportation/starship_list.html'

  def get_context_data(self, **kwargs):
    context = super(StarshipCategoryView, self).get_context_data(**kwargs)
    context['starship_list'] = [i for i in context['starship_list'] if i.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
    return context


class VehicleAttachmentListView(ListView):
  model = VehicleAttachment

  def get_context_data(self, **kwargs):
    context = super(VehicleAttachmentListView, self).get_context_data(**kwargs)
    context.update(sorting_context(VehicleAttachment, 7, 'name', ['name', 'price', 'hard_points', 'rarity', 'index'], ['index'], self.request))
    return context 

class VehicleAttachmentCategoryView(VehicleAttachmentListView):
  model = VehicleAttachment
  template_name = 'transportation/vehicleattachment_list.html'

  def get_context_data(self, **kwargs):
    context = super(VehicleAttachmentCategoryView, self).get_context_data(**kwargs)
    context['vehicleattachment_list'] = [i for i in context['vehicleattachment_list'] if i.category.id == int(self.kwargs['category'])]
    context['category'] = Category.objects.get(pk=self.kwargs['category'])
    return context

class VehicleAttachmentDetailView(DetailView):
  model = VehicleAttachment

class CategoryListView(ListView):
  queryset = Category.objects.filter(model__in=Category.model_numbers()).order_by('model', 'name')
