from django.shortcuts import render
from django.views.generic import ListView, DetailView

from base.models import *

class BookDetailView(DetailView):
  model = Book
  
  def get_context_data(self, **kwargs):
    context = super(BookDetailView, self).get_context_data(**kwargs)
    object = self.get_object()
    context['entry_list'] = object.entry_set
    context['request'] = self.request
    return context

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
    object_list = model_class.objects.filter(model=model_class.__name__).order_by(order_by, default_sort)
  elif order_by == 'index':
    object_list = [x for x in [model_class.objects.get(pk=x.entry.id) for x in Index.objects.filter(entry__model=model_class.__name__)]]
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

