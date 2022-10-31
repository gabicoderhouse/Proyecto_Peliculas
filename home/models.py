from django.db import models
from ckeditor.fields import RichTextField

class Pelicula(models.Model):
    nombre = models.CharField(max_length=60)
    genero = models.CharField(max_length=30)
    resumen = RichTextField(null=True)
    anio_estreno = models.IntegerField()    
    duracion = models.IntegerField()
    clasificacion_edad = models.IntegerField()
    imagen = models.ImageField(upload_to='peliculas',null=True, blank=True)
    
    def __str__(self):
        return f'Nombre: {self.nombre} - Género: {self.genero}' 