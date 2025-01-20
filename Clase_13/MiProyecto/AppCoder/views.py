from django.shortcuts import render, redirect
from .forms import *
from .models import Estudiante, Profesor, Profile
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# ==================================INDEX=================================================
@login_required
def index(request):
    return render(request, 'AppCoder/index.html')


#================================REGISTRO================
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Usuario creado exitosamente. ¡Ahora puedes iniciar sesión!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'AppCoder/register.html', {'form': form})


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
@login_required
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
# or | and & not !
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


#=============================EDITAR PERFiLE =================================
from .forms import UserEditForm, ProfileEditForm

@login_required
def editarPerfil(request):
    usuario = request.user
    try:
        perfil = usuario.profile
    except Profile.DoesNotExist:
        perfil = Profile.objects.create(user=usuario)

    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=usuario)
        profile_form = ProfileEditForm(request.POST, request.FILES, instance=perfil)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('index')
    else:
        user_form = UserEditForm(instance=usuario)
        profile_form = ProfileEditForm(instance=perfil)

    return render(request, "AppCoder/editarPerfil.html", {
        "user_form": user_form,
        "profile_form": profile_form,
        "usuario": usuario
    })
