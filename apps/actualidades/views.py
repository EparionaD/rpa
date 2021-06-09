from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import TemplateView, DetailView
from .models import Actualidades

class ActualidadesView(TemplateView):
    template_name = 'actualidades/actualidades.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actualidades'] = Actualidades.objects.filter(state=True).order_by('-date_create')

        paginacion = Paginator(context['actualidades'],6)
        page = self.request.GET.get('page')
        context['actualidades'] = paginacion.get_page(page)

        return context

class ActualidadesDetailView(DetailView):
    model = Actualidades
    template_name = 'actualidades/detalle.html'
    context_object_name = 'detalle'
