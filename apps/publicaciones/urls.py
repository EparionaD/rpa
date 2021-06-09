from django.urls import path
from .views import PublicacionesView, PublicacionesDetailView

urlpatterns = [
    path('', PublicacionesView.as_view(), name="publicaciones"),
    path('<slug:slug>/', PublicacionesDetailView.as_view(), name="detalle"),
]