from django import forms

class FormPelicula(forms.Form):
    nombre = forms.CharField(max_length=60, label='Nombre')
    genero = forms.CharField(max_length=30, label='Género')
    resumen = forms.CharField(max_length=200, label='Resumen')
    anio_estreno = forms.IntegerField(label='Año Estreno')    
    duracion = forms.IntegerField(label='Duración(min)')
    clasificacion_edad = forms.IntegerField(label='Mayores de') 
    
    
class BusquedaPelicula(forms.Form):
    nombre = forms.CharField(max_length=60, required=False)