#from typing_extensions import Required
from xml.dom.pulldom import default_bufsize
from django.db import models
from ckeditor.fields import RichTextField
from django.forms import NullBooleanField
from pkg_resources import require
from django.contrib.auth.models import User

class Pelicula(models.Model):
    nombre = models.CharField(max_length=60)
    genero = models.CharField(max_length=30)
    resumen = RichTextField(null=True)
    anio_estreno = models.IntegerField()    
    duracion = models.IntegerField()
    clasificacion_edad = models.IntegerField()
    imagen = models.ImageField(upload_to='peliculas',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fe_alta= models.DateTimeField(null=True)
    fe_cambio=models.DateTimeField(null=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Género: {self.genero}' 