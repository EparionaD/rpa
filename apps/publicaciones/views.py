from django.core.paginator import Paginator
from django.views.generic import TemplateView, DetailView
from .models import Publicaciones, Categorias

class PublicacionesView(TemplateView):
    template_name = 'publicaciones/publicaciones.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorias.objects.all().order_by('date_create')
        context['publicaciones'] = Publicaciones.objects.filter(state=True).order_by('-date_create')
        context['jurisprudencia'] = Publicaciones.objects.filter(categorias__slug='jurisprudencia').filter(state=True).order_by('-date_create')
        context['boletines'] = Publicaciones.objects.filter(categorias__slug='boletines').filter(state=True).order_by('-date_create')
        context['articulos'] = Publicaciones.objects.filter(categorias__slug='articulos').filter(state=True).order_by('-date_create')

        # paginacionjuri = Paginator(context['jurisprudencia'],6)
        # pagejuri = self.request.GET.get('page')
        # context['jurisprudencia'] = paginacionjuri.get_page(pagejuri)
        
        # paginacionbole = Paginator(context['boletines'],6)
        # pagebole = self.request.GET.get('page')
        # context['boletines'] = paginacionbole.get_page(pagebole)

        # paginacionarti = Paginator(context['articulos'],6)
        # pagearti = self.request.GET.get('page')
        # context['articulos'] = paginacionarti.get_page(pagearti)

        return context

class PublicacionesList(TemplateView):
    template_name = 'publicaciones/lista.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorias.objects.all().order_by('date_create')
        context['publicaciones'] = Publicaciones.objects.filter(categorias__slug=kwargs['slug']).filter(state=True).order_by('-date_create')

        paginacionpublicaciones = Paginator(context['publicaciones'],6)
        pagepublicaciones = self.request.GET.get('page')
        context['publicaciones'] = paginacionpublicaciones.get_page(pagepublicaciones)

        return context

# class PublicacionesDetailView(DetailView):
#     model = Publicaciones
#     template_name = 'publicaciones/detalle.html'
#     context_object_name = 'detalle'

class PublicacionesDetailView(TemplateView):
    template_name = 'publicaciones/detalle.html'

    def get_context_data(self, **kwargs):
        cat = kwargs['publi_slug']
        print(cat)
        context = super().get_context_data(**kwargs)
        context['detalle'] = Publicaciones.objects.filter(categorias__slug=kwargs['slug']).get(publi_slug=kwargs['publi_slug'])

        return context