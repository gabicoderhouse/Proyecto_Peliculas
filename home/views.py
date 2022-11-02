from django.shortcuts import redirect, render
from home.models import Pelicula
from home.forms import FormPelicula, BusquedaPelicula
from django.contrib.auth.decorators import login_required
from django.views.generic import  DetailView
from datetime import datetime

def ver_peliculas(request):
    
    nombre = request.GET.get('nombre', None)
    
    if nombre:
        peliculas = Pelicula.objects.filter(nombre__icontains=nombre)
    else:
        peliculas = Pelicula.objects.all()
        
    formulario = BusquedaPelicula()
    
    return render(request, 'home/ver_peliculas.html', {'peliculas': peliculas, 'formulario': formulario})

@login_required
def crear_pelicula(request):
    
    if request.method == 'POST':
        formulario = FormPelicula(request.POST, request.FILES)
        if formulario.is_valid():
            datos = formulario.cleaned_data
            pelicula = Pelicula(
                nombre=datos['nombre'],
                genero=datos['genero'],
                anio_estreno=datos['anio_estreno'],
                duracion=datos['duracion'],
                clasificacion_edad=datos['clasificacion_edad'],
                imagen=datos['imagen'],
                resumen=datos['resumen'],
                user = request.user,
                fe_alta = datetime.now()
            )
            pelicula.save()
            return redirect('ver_peliculas')
        else:
            return render(request, 'home/crear_pelicula.html', {'formulario': formulario})
    
    formulario = FormPelicula()
    
    return render(request, 'home/crear_pelicula.html', {'formulario': formulario})

@login_required
def editar_pelicula(request, id):
    
    pelicula = Pelicula.objects.get(id=id)
    
    if pelicula.user.id != request.user.id and not request.user.is_superuser :
        return redirect('ver_peliculas')
    else:    
        if request.method == 'POST':
            formulario = FormPelicula(request.POST, request.FILES)
            if formulario.is_valid():
                datos = formulario.cleaned_data        
                pelicula.nombre = datos['nombre']
                pelicula.genero = datos['genero']
                pelicula.anio_estreno = datos['anio_estreno']
                pelicula.duracion = datos['duracion']
                pelicula.clasificacion_edad = datos['clasificacion_edad']
                pelicula.resumen = datos['resumen']
                pelicula.imagen = datos['imagen']
                pelicula.user = request.user
                pelicula.fe_cambio = datetime.now()
                pelicula.save()
                return redirect('ver_peliculas')
            else:
                return render(request, 'home/editar_pelicula.html', {'formulario': formulario})   
    
    formulario =  FormPelicula(
        initial={
            'nombre': pelicula.nombre,
            'genero': pelicula.genero,
            'resumen': pelicula.resumen,
            'anio_estreno': pelicula.anio_estreno,
            'duracion': pelicula.duracion,
            'clasificacion_edad': pelicula.clasificacion_edad,
            'imagen': pelicula.imagen
        }
    )
    
    return render(request, 'home/editar_pelicula.html', {'formulario': formulario, 'pelicula': pelicula})
    
@login_required    
def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    if pelicula.user.id != request.user.id and not request.user.is_superuser :
        return redirect('ver_peliculas')
    else:   
        pelicula.delete()
        return redirect('ver_peliculas')
  
def acerca_de(request):   
    return render(request, 'home/acerca_de.html')      
  
def index(request):    
    return render(request, 'home/index.html')    

class VerPelicula(DetailView):
    model = Pelicula
    template_name = 'home/ver_una_pelicula.html'