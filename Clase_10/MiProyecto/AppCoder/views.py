from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import EstudianteForm, ProfesorForm
from .models import Estudiante, Profesor

def cargar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
    else:
        form = EstudianteForm()
    return render(request, 'AppCoder/estudiante_form.html', {'form': form})

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'AppCoder/estudiantes_list.html', {'estudiantes': estudiantes})

def cargar_profesor(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_profesores')
    else:
        form = ProfesorForm()
    return render(request, 'AppCoder/profesor_form.html', {'form': form})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'AppCoder/profesores_list.html', {'profesores': profesores})


def index(request):
    return render(request, 'AppCoder/index.html')