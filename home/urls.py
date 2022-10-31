from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver_peliculas/', views.ver_peliculas, name='ver_peliculas'),
    path('ver_peliculas/ver/<int:pk>', views.VerPelicula.as_view(), name='ver_una_pelicula'),
    path('crear_peliculas/', views.crear_pelicula, name='crear_pelicula'),
    path('ver_peliculas/editar_pelicula/<int:id>', views.editar_pelicula, name='editar_pelicula'),
    path('ver_peliculas/eliminar_pelicula/<int:id>', views.eliminar_pelicula, name='eliminar_pelicula'),
    path('acerca_de/', views.acerca_de, name='acerca_de'),
]