from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Sum

from books.models import *
from equipment.models import *

def index(request):
  return HttpResponse("Hello, world. You're at the FFG SWRPG index.")
  
class BookListView(ListView):
  model = Book
  
class BookDetailView(DetailView):
  model = Book
  
  def get_context_data(self, **kwargs):
    context = super(BookDetailView, self).get_context_data(**kwargs)
    object = self.get_object()
    context['gear_list'] = object.gear_set
    context['weapon_list'] = object.weapon_set
    context['armor_list'] = object.armor_set
    context['attachment_list'] = object.attachment_set
    context['vehicle_list'] = object.vehicle_set
    context['starship_list'] = object.starship_set
    context['skill_list'] = object.skill_set
    context['talent_list'] = object.talent_set
    context['ability_list'] = object.ability_set
    context['adversary_list'] = object.adversary_set
    context['creature_list'] = object.creature_set
    context['request'] = self.request
    return context
  
  

