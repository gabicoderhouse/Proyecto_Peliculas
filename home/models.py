from django.db import models

class Pelicula(models.Model):
    nombre = models.CharField(max_length=60)
    genero = models.CharField(max_length=30)
    resumen = models.CharField(max_length=200)
    anio_estreno = models.IntegerField()    
    duracion = models.IntegerField()
    clasificacion_edad = models.IntegerField() 
