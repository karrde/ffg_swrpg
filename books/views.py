from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from books.models import Item, Category, Weapon, Book, Armor, Attachment, Vehicle, Starship

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
  
class ItemListView(ListView):
  queryset = Item.objects.filter(category__model=1)
  
  def get_context_data(self, **kwargs):
    context = super(ItemListView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    context['item_list'] = Item.objects.filter(category__model=1).order_by(order_by, 'name')
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
    order_by = self.request.GET.get('order_by', 'name')
    context['weapon_list'] = Weapon.objects.filter(category__model=2).order_by(order_by, 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
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
    order_by = self.request.GET.get('order_by', 'name')
    context['armor_list'] = Armor.objects.filter(category__model=3).order_by(order_by, 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    return context 

class ArmorDetailView(DetailView):
  model = Armor

class AttachmentListView(ListView):
  model = Attachment

  def get_context_data(self, **kwargs):
    context = super(AttachmentListView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    context['attachment_list'] = Attachment.objects.filter(category__model=4).order_by(order_by, 'name')
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
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    context['vehicle_list'] = Vehicle.objects.filter(category__model=5) #.order_by(order_by, 'name')
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
    order_by = self.request.GET.get('order_by', 'name')
    if order_by.startswith("-"):
      order_by = order_by.lstrip("-")
      context['reverse'] = True
    context['order_by'] = order_by
    context['request'] = self.request
    context['starship_list'] = Starship.objects.filter(category__model=6) #.order_by(order_by, 'name')
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

