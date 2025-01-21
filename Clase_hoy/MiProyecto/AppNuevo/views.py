from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Autor

class AutorListView(ListView):
    model = Autor
    template_name = 'AppNuevo/autor_list.html'
    context_object_name = 'autors'

class AutorDetailView(DetailView):
    model = Autor
    template_name = 'AppNuevo/autor_detail.html'

class AutorCreateView(CreateView):
    model = Autor
    template_name = 'AppNuevo/autor_form.html'
    fields = ['nombre', 'descripcion', 'correo']
    success_url = reverse_lazy('autor_list')

class AutorUpdateView(UpdateView):
    model = Autor
    template_name = 'AppNuevo/autor_form.html'
    fields = ['nombre', 'descripcion', 'correo']
    success_url = reverse_lazy('autor_list')

class AutorDeleteView(DeleteView):
    model = Autor
    template_name = 'AppNuevo/autor_delete.html'
    success_url = reverse_lazy('autor_list')
