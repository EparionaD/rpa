from django.shortcuts import render
from django.views.generic import TemplateView
from apps.actualidades.models import Actualidades
from apps.publicaciones.models import Publicaciones, Categorias

class InicioView(TemplateView):
    template_name = 'inicio/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actualidades'] = Actualidades.objects.filter(state=True).order_by('-date_create')
        context['categorias'] = Categorias.objects.all().order_by('date_create')
        context['jurisprudencia'] = Publicaciones.objects.filter(categorias__slug='jurisprudencia').filter(state=True).order_by('-date_create')
        context['boletines'] = Publicaciones.objects.filter(categorias__slug='boletines').filter(state=True).order_by('-date_create')
        context['articulos'] = Publicaciones.objects.filter(categorias__slug='articulos').filter(state=True).order_by('-date_create')

        return context

class FirmaView(TemplateView):
    template_name = 'inicio/firma.html'

class EspecialidadesView(TemplateView):
    template_name = 'inicio/especialidades.html'

class ContactoView(TemplateView):
    template_name = 'inicio/contacto.html'