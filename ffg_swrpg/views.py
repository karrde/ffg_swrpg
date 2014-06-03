from django.shortcuts import render
from blog.models import Blog

def index_view(request):
    return render(request, 'ffg_swrpg/index.html', {'blog_list': Blog.objects.order_by('-posting_date')[:5]})