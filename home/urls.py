from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver_peliculas/', views.ver_peliculas, name= 'ver_peliculas'),
    path('crear_pelicula/', views.crear_pelicula, name= 'crear_pelicula'),
    path('ver_peliculas/editar_pelicula/<int:id>', views.editar_pelicula, name= 'editar_pelicula'),
    path('ver_peliculas/eliminar_pelicula/<int:id>', views.eliminar_pelicula, name= 'eliminar_pelicula')
]