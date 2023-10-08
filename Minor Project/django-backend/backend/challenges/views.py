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

def codeEditor(request):
    return render(request, "pages/code editor.html")

def customRoom(request):
    return render(request, "pages/custom room.html")

def challenges(request):
    return render(request, "pages/challenges.html")

def login(request):
    return render(request, "pages/login signup.html")

def contact(request):
    return render(request, "pages/contact us.html")
