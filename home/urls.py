from django.urls import path
from home import views

urlpatterns = [
    path('', views.index),
    path('ver_peliculas/', views.ver_peliculas, name='ver_peliculas'),
    path('crear_peliculas/', views.crear_pelicula, name='crear_pelicula'),
    path('editar_pelicula/<int:pk>', views.editar_pelicula, name='editar_pelicula'),
    path('eliminar_pelicula/<int:pk>', views.eliminar_pelicula, name='eliminar_pelicula')
]