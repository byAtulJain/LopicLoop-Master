#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import ResourceCard

def index(request):
    return render(request, "index.html")

def learningResources(request):
    data = ResourceCard.objects.all()
    context = {"data": data}
    return render(request, "pages/learningResources.html",context)