from django.urls import path
from .views import EquivoView, EquipoDetailView

urlpatterns = [
    path('', EquivoView.as_view(), name="equipo"),
    path('<slug:slug>/', EquipoDetailView.as_view(), name="detalle"),
]