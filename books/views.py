from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from books.models import Item, Category, Weapon, Book

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
    return context
  
class ItemListView(ListView):
  queryset = Item.objects.filter(category__model=1)
  
  def get_context_data(self, **kwargs):
    context = super(ItemListView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    context['item_list'] = Item.objects.filter(category__model=1).order_by(order_by, 'name')
    return context 
  
class ItemByCategoryView(ListView):
  queryset = Category.objects.filter(model=1)
  template_name = 'books/item_by_category_list.html'

  def get_context_data(self, **kwargs):
    context = super(ItemByCategoryView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    context['order_by'] = order_by
    return context
  
class ItemDetailView(DetailView):
  model = Item

class ItemCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/item_category_detail.html'

  def get_context_data(self, **kwargs):
    context = super(ItemCategoryDetailView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    context['order_by'] = order_by
    return context

class WeaponListView(ListView):
  model = Weapon

class WeaponByCategoryView(ListView):
  queryset = Category.objects.filter(model=2)
  template_name = 'books/weapon_by_category_list.html'

  def get_context_data(self, **kwargs):
    context = super(WeaponByCategoryView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    context['order_by'] = order_by
    return context

class WeaponDetailView(DetailView):
  model = Weapon

class WeaponCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/weapon_category_detail.html'

  def get_context_data(self, **kwargs):
    context = super(WeaponCategoryDetailView, self).get_context_data(**kwargs)
    order_by = self.request.GET.get('order_by', 'name')
    context['order_by'] = order_by
    return context
