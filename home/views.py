from django.shortcuts import render
from home.models import Pelicula
from home.forms import FormPelicula, BusquedaPelicula


def index(request):
    return render(request, 'home/index.html')

def ver_peliculas(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        peliculas = Pelicula.objects.filter(nombre__icontains=nombre)
    else:
        peliculas = Pelicula.objects.all()
    
    formulario = BusquedaPelicula()
    
    return render(request, 'home/ver_peliculas.html', {'pelculas': peliculas, 'formulario':formulario})