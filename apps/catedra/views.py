from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import Catedra, Categorias

class CatedraView(TemplateView):
    template_name = 'catedra/catedra.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorias.objects.all().order_by('date_create')
        context['cursos'] = Catedra.objects.filter(categorias__slug='cursos').filter(state=True).order_by('-date_create')
        context['seminarios'] = Catedra.objects.filter(categorias__slug='seminarios').filter(state=True).order_by('-date_create')
        context['conversatorios'] = Catedra.objects.filter(categorias__slug='conversatorios').filter(state=True).order_by('-date_create')

        return context

class CatedraDetailView(DetailView):
    model = Catedra
    template_name = 'catedra/detalle.html'
    context_object_name = 'detalle'