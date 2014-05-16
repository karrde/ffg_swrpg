from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from books.models import Item, Category, Weapon

def index(request):
  return HttpResponse("Hello, world. You're at the FFG SWRPG index.")
  
class ItemListView(ListView):
  model = Item
  
class ItemByCategoryView(ListView):
  queryset = Category.objects.filter(model=1)
  template_name = 'books/item_by_category_list.html'

# def get_context_data(self, **kwargs):
#     # Call the base implementation first to get a context
#     context = super(ListView, self).get_context_data(**kwargs)
#     context['items_by_category'] = {}
#     for category in context['queryset']:
#       context['items_by_category'][category.name] = Item.objects.filter(category=category.id)
#     return context
  
  
class ItemDetailView(DetailView):
  model = Item

class ItemCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/item_category_detail.html'

class WeaponListView(ListView):
  model = Weapon

class WeaponByCategoryView(ListView):
  queryset = Category.objects.filter(model=2)
  template_name = 'books/weapon_by_category_list.html'

class WeaponDetailView(DetailView):
  model = Weapon

class WeaponCategoryDetailView(DetailView):
  model = Category
  template_name = 'books/weapon_category_detail.html'
