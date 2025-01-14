from django.urls import path
from .views import cargar_estudiante, lista_estudiantes, cargar_profesor, lista_profesores, index, buscar
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', index, name='index'),
    path('cargar_estudiante', cargar_estudiante, name = 'cargar_estudiante'),
    path('estudiantes/', lista_estudiantes, name = 'lista_estudiantes'),
    path('cargar_profesor/', cargar_profesor, name = 'cargar_profesor'),
    path('profesores/', lista_profesores, name='lista_profesores'),
    path('buscar/', buscar, name='buscar'),
    path('login/', LoginView.as_view(template_name='AppCoder/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
