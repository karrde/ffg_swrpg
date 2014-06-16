from django.shortcuts import render
from blog.models import Blog
from django.views.generic import ListView, DetailView
from django.http import HttpResponse


def index_view(request):
  return render(request, 'ffg_swrpg/index.html', {'blog_list': Blog.objects.order_by('-posting_date')[:5]})
    
class BlogDetailView(DetailView):
    model = Blog
    template_name = 'ffg_swrpg/blog_detail.html'