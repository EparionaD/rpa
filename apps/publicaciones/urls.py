from django.urls import path
from .views import PublicacionesView, PublicacionesList, PublicacionesDetailView

urlpatterns = [
    path('', PublicacionesView.as_view(), name="publicaciones"),
    path('<slug:slug>/<slug:publi_slug>/', PublicacionesDetailView.as_view(), name="detalle"),
    path('<slug:slug>/', PublicacionesList.as_view(), name="categorias"),
]