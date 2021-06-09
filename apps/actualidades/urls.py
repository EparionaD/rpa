from django.urls import path
from .views import ActualidadesView, ActualidadesDetailView

urlpatterns = [
    path('', ActualidadesView.as_view(), name="actualidades"),
    path('<slug:slug>/', ActualidadesDetailView.as_view(), name="detalle"),
]