from django.shortcuts import redirect, render
from home.models import Pelicula
from home.forms import FormPelicula, BusquedaPelicula

from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

def ver_peliculas(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        pelicula = Pelicula.objects.filter(nombre__icontains=nombre)
    else:
        pelicula = Pelicula.objects.all()
        
    formulario = BusquedaPelicula()
    
    return render(request, 'home/ver_perliculas.html', {'pelicula': pelicula, 'formulario': formulario})

def crear_pelicula(request):
    
    if request.method == 'POST':
        formulario = FormPelicula(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            pelicula = Pelicula(
                nombre=datos['nombre'],
                genero=datos['genero'],
                resumen=datos['resumen'],
                anio_estreno=datos['anio_estreno'],
                duracion=datos['duracion'],
                clasificacion_edad=datos['clasificacion_edad']
            )
            pelicula.save()
            return redirect('ver_peliculas')
        else:
            return render(request, 'home/crear_pelicula.html', {'formulario': formulario})
    
    formulario = FormPelicula()
    
    return render(request, 'home/crear_pelicula.html', {'formulario': formulario})

def editar_pelicula(request, id):
    
    pelicula = Pelicula.objects.get(id=id)
    
    if request.method == 'POST':
        formulario = FormPelicula(request.POST)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            
            pelicula.nombre = datos['nombre']
            pelicula.genero = datos['genero']
            pelicula.resumen = datos['resumen']
            pelicula.anio_estreno = datos['anio_estreno']
            pelicula.duracion = datos['duracion']
            pelicula.clasificacion_edad = datos['clasificacion_edad']
            pelicula.save()
            
            return redirect('ver_peliculas')
        else:
            return render(request, 'home/editar_pelicula.html', {'formulario': formulario})
            
    
    formulario =  FormPelicula(
        initial={
            'nombre': pelicula.nombre,
            'tipo': pelicula.genero,
            'edad': pelicula.resumen,
            'fecha_nacimiento': pelicula.anio_estreno,
            'duracion': pelicula.duracion,
            'clasificacion_edad': pelicula.clasificacion_edad
        }
    )
    
    return render(request, 'home/editar_pelicula.html', {'formulario': formulario, 'pelicula': pelicula})
    
def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('ver_peliculas')
  
def index(request):
    
    return render(request, 'home/index.html')    