from django.shortcuts import render
from .models import Equipo
from django.views.generic import ListView, DetailView

class EquivoView(ListView):
    model = Equipo
    template_name = 'equipo/equipo.html'
    context_object_name = 'equipos'

class EquipoDetailView(DetailView):
    model = Equipo
    template_name = 'equipo/detalle.html'
    context_object_name = 'detalle'