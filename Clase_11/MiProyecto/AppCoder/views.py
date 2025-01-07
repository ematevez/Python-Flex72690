from django.shortcuts import render, redirect
from .forms import EstudianteForm, ProfesorForm
from .models import Estudiante, Profesor
from django.db.models import Q


# ==================================INDEX=================================================

def index(request):
    return render(request, 'AppCoder/index.html')



# =============================ESTUDIANTE=CARGA ESTUDIANTE================================================
def cargar_estudiante(request):
    if request.method == 'POST':
        form = EstudianteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_estudiantes')
            # return redirect('index')
    else:
        form = EstudianteForm()
    return render(request, 'AppCoder/estudiante_form.html', {'form': form})


# ==========================LISTA===ESTUDIANTE=================================================

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



# =============================BUSQUEDA=================================================
def buscar(request):
    query = request.GET.get('q', '')
    resultados = []

    if query:
        estudiantes = Estudiante.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query)
        )
        profesores = Profesor.objects.filter(
            Q(nombre__icontains=query) | Q(apellido__icontains=query) | Q(email__icontains=query) | Q(profesion__icontains=query) | Q(direccion__icontains=query)
        )

        for estudiante in estudiantes:
            resultados.append({
                'tipo': 'Estudiante',
                'nombre': estudiante.nombre,
                'apellido': estudiante.apellido,
                'email': estudiante.email,
                'extra': '-',
            })

        for profesor in profesores:
            resultados.append({
                'tipo': 'Profesor',
                'nombre': profesor.nombre,
                'apellido': profesor.apellido,
                'email': profesor.email,
                'extra': f'{profesor.profesion} / {profesor.direccion}',
            })

    return render(request, 'AppCoder/index.html', {'resultados': resultados})
