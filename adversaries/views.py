from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from django.db.models import Sum

# Create your views here.
from base.models import Index
from adversaries.models import *

class AdversaryDetailView(DetailView):
  model = Adversary

class AdversaryListView(ListView):
  model = Adversary
  
  
