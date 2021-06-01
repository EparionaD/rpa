from django.urls import path
from .views import EspecialidadesView, InicioView, FirmaView, ContactoView

urlpatterns = [
    path('', InicioView.as_view(), name="inicio"),
    path('firma/', FirmaView.as_view(), name="firma"),
    path('especialidades/', EspecialidadesView.as_view(), name="especialidades"),
    path('contacto/', ContactoView.as_view(), name="contacto"),
]