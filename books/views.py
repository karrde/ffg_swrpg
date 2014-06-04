from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Sum
from books.models import *

def index(request):
  return HttpResponse("Hello, world. You're at the FFG SWRPG index.")
  
class BookListView(ListView):
  model = Book
  
class BookDetailView(DetailView):
  model = Book
  
  def get_context_data(self, **kwargs):
    context = super(BookDetailView, self).get_context_data(**kwargs)
    object = self.get_object()
    context['item_list'] = object.item_set
    context['weapon_list'] = object.weapon_set
    context['armor_list'] = object.armor_set
    context['attachment_list'] = object.attachment_set
    context['vehicle_list'] = object.vehicle_set
    context['starship_list'] = object.starship_set
    context['request'] = self.request
    return context
  
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
    object_list = [model_class.objects.get(pk=x.item.id) for x in Index.objects.filter(item__category__model=category_model)]
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
    context['item_list'] = context['item_list'].filter(category__id=self.kwargs['category'])
    return context

class ItemByCategoryView(ListView):
  queryset = Category.objects.filter(model=1)
  template_name = 'books/item_by_category_list.html'

  def get_context_data(self, **kwargs):
    context = super(ItemByCategoryView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context
  
class ItemDetailView(DetailView):
  model = Item

class ItemCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/item_category_detail.html'

  def get_context_data(self, **kwargs):
    context = super(ItemCategoryDetailView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

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
    context['weapon_list'] = context['weapon_list'].filter(category__id=self.kwargs['category'])
    return context
  

class WeaponByCategoryView(ListView):
  queryset = Category.objects.filter(model=2)
  template_name = 'books/weapon_by_category_list.html'

  def get_context_data(self, **kwargs):
    context = super(WeaponByCategoryView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

class WeaponDetailView(DetailView):
  model = Weapon

class WeaponCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/weapon_category_detail.html'

  def get_context_data(self, **kwargs):
    context = super(WeaponCategoryDetailView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

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
    context['attachment_list'] = context['attachment_list'].filter(category__id=self.kwargs['category'])
    return context

class AttachmentByCategoryView(ListView):
  queryset = Category.objects.filter(model=4)
  template_name = 'books/attachment_by_category_list.html'

  def get_context_data(self, **kwargs):
    context = super(AttachmentByCategoryView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

class AttachmentDetailView(DetailView):
  model = Attachment

class AttachmentCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/attachment_category_detail.html'

  def get_context_data(self, **kwargs):
    context = super(AttachmentCategoryDetailView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

class VehicleDetailView(DetailView):
  model = Vehicle
  
class VehicleListView(ListView):
  model = Vehicle

  def get_context_data(self, **kwargs):
    context = super(VehicleListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Vehicle, 5, 'name', ['name', 'silhoutte', 'speed', 'handling', 'model', 'manufacturer', 'passenger', 'price', 'encumbrance', 'rarity', 'weapon_count', 'crew', 'index'], ['index', 'crew'], self.request))
    return context 

class VehicleCategoryView(VehicleListView):
  model = Vehicle
  template_name = 'books/vehicle_list.html'

  def get_context_data(self, **kwargs):
    context = super(VehicleCategoryView, self).get_context_data(**kwargs)
    context['vehicle_list'] = context['vehicle_list'].filter(category__id=self.kwargs['category'])
    return context

class VehicleByCategoryView(ListView):
  queryset = Category.objects.filter(model=5)
  template_name = 'books/vehicle_by_category_list.html'

  def get_context_data(self, **kwargs):
    context = super(VehicleByCategoryView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

class VehicleCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/vehicle_category_detail.html'

  def get_context_data(self, **kwargs):
    context = super(VehicleCategoryDetailView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

class StarshipDetailView(DetailView):
  model = Starship

class StarshipListView(ListView):
  model = Starship

  def get_context_data(self, **kwargs):
    context = super(StarshipListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Starship, 6, 'name', ['name', 'silhoutte', 'speed', 'handling', 'model', 'manufacturer', 'passenger', 'price', 'encumbrance', 'rarity', 'weapon_count', 'crew', 'navicomputer', 'index'], ['index', 'crew'], self.request))
    return context 

class StarshipCategoryView(StarshipListView):
  model = Starship
  template_name = 'books/starship_list.html'

  def get_context_data(self, **kwargs):
    context = super(StarshipCategoryView, self).get_context_data(**kwargs)
    context['starship_list'] = context['starship_list'].filter(category__id=self.kwargs['category'])
    return context

class StarshipByCategoryView(ListView):
  queryset = Category.objects.filter(model=6)
  template_name = 'books/starship_by_category_list.html'

  def get_context_data(self, **kwargs):
    context = super(StarshipByCategoryView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

class StarshipCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/starship_category_detail.html'

  def get_context_data(self, **kwargs):
    context = super(StarshipCategoryDetailView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context

