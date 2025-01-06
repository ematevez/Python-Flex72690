from django.urls import path
from .views import cargar_estudiante, lista_estudiantes, cargar_profesor, lista_profesores, index, buscar


urlpatterns = [
    path('', index, name='index'),
    path('buscar/', buscar, name='buscar'),
    path('cargar_estudiante', cargar_estudiante, name = 'cargar_estudiante'),
    path('estudiantes/', lista_estudiantes, name = 'lista_estudiantes'),
    path('cargar_profesor/', cargar_profesor, name = 'cargar_profesor'),
    path('profesores/', lista_profesores, name='lista_profesores'),
]
