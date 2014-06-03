from django.shortcuts import render

def index_view(request):
    # View code here...
    return render(request, 'ffg_swrpg/index.html')