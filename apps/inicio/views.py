from django.shortcuts import render
from django.views.generic import TemplateView

class InicioView(TemplateView):
    template_name = 'inicio/index.html'

class FirmaView(TemplateView):
    template_name = 'inicio/firma.html'

class EspecialidadesView(TemplateView):
    template_name = 'inicio/especialidades.html'

class ContactoView(TemplateView):
    template_name = 'inicio/contacto.html'