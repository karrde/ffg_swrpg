from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
from base.models import Index
from equipment.views import sorting_context
from adversaries.models import *

class AdversaryDetailView(DetailView):
  model = Adversary

class AdversaryListView(ListView):
  model = Adversary
  
  def get_context_data(self, **kwargs):
    context = super(AdversaryListView, self).get_context_data(**kwargs)
    context.update(sorting_context(Adversary, 'name', ['name', 'level', 'index'], ['index'], self.request))
    return context 
  
