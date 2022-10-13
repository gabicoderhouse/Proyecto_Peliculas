from django.shortcuts import render, redirect
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
    
    return render(request, 'home/ver_peliculas.html', {'peliculas': peliculas, 'formulario':formulario})

def crear_pelicula(request):
    
    if request.method == 'POST':
        
        formulario = FormPelicula(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            nombre = data['nombre']
            genero = data['genero']
            resumen = data['resumen']
            anio_estreno = data['anio_estreno']
            duracion = data['duracion']
            clasificacion_edad = data['clasificacion_edad']
            
            pelicula = Pelicula(nombre=nombre, 
                                genero=genero, 
                                resumen=resumen, 
                                anio_estreno=anio_estreno,
                                duracion=duracion,
                                clasificacion_edad=clasificacion_edad)
            pelicula.save()
            
            return redirect('ver_peliculas')
    
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
    
    formulario = FormPelicula(
        initial={
            'nombre': pelicula.nombre,
            'genero': pelicula.genero,
            'resumen': pelicula.resumen,
            'anio_estreno': pelicula.anio_estreno,
            'duracion' : pelicula.duracion,
            'clasificacion_edad' : pelicula.clasificacion_edad
        }
    )
    
    return render(request, 'home/editar_pelicula.html', {'formulario': formulario, 'pelicula': pelicula})
    
def eliminar_pelicula(request, id):
    pelicula = Pelicula.objects.get(id=id)
    pelicula.delete()
    return redirect('ver_peliculas')
            
