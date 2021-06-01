from django.urls import path
from .views import CatedraView, CatedraDetailView

urlpatterns = [
    path('', CatedraView.as_view(), name="catedra"),
    path('<slug:slug>/', CatedraDetailView.as_view(), name="detalle"),
]