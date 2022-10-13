from django.shortcuts import render
#from home.models import Familiar

def hola_mundo(request):
    return render(request, 'home/hola.html' )

def index(request):
    return render(request, 'home/index.html')