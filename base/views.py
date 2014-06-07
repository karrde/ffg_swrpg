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
