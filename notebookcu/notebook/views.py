#from django.http import HttpResponse
from django.shortcuts import render
from .models import Notebook

# Create your views here.



def index(request):
    return render(request,'index.html')

def search_venues(request):
    return render(request,'notebook/search_venues.html',{})

def notebook(request):
    notebooks = Notebook.objects.all()
    context = {
        "notebooks" : notebooks
    }
    return render(request, 'notebook.html', context)

def notebook_details(request, id):
    notebook = Notebook.objects.get(pk=id)
    context = {
        "notebook" : notebook
    }
    return render(request,'notebook-details.html', context)

def notebook_min(request):
    notebooks = Notebook.objects.all().order_by("fiyat")
    context = {
        "notebooks" : notebooks
    }
    return render(request, 'notebook-min.html', context)

def notebook_max(request):
    notebooks = Notebook.objects.all().order_by("-fiyat")
    context = {
        "notebooks" : notebooks
    }
    return render(request, 'notebook-min.html', context)

def notebook_puan(request):
    notebooks = Notebook.objects.all().order_by("-puan")
    context = {
        "notebooks" : notebooks
    }
    return render(request, 'notebook-puan.html', context)