from django.shortcuts import render, redirect
from .forms import EstudianteForm, ProfesorForm
from .models import Estudiante, Profesor
# Create your views here.

# ==================================INDEX=================================================

def index(request):
    return render(request, 'AppCoder/index.html')



# =============================ESTUDIANTE=================================================
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
    return render(request, 'AppCoder/lista_estudiantes.html', {'estudiantes': estudiantes})


# =============================PROFESOR=================================================
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
    return render(request, 'AppCoder/lista_profesores.html', {'profesores': profesores})