from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver_peliculas/', views.ver_peliculas, name= 'ver_peliculas'),
]