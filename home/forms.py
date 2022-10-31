from django import forms
from ckeditor.fields import RichTextFormField

from home.models import Pelicula

class FormPelicula(forms.Form):
    nombre = forms.CharField(max_length=60, label='Nombre')
    genero = forms.CharField(max_length=30, label='Género')
    anio_estreno = forms.IntegerField(label='Año Estreno')    
    duracion = forms.IntegerField(label='Duración(min)')
    clasificacion_edad = forms.IntegerField(label='Mayores de') 
    resumen=RichTextFormField(required=False)
    imagen=forms.ImageField(required=False)

    
    
class BusquedaPelicula(forms.Form):
    nombre = forms.CharField(max_length=60, required=False)
    
