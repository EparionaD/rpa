from django.contrib import admin
from .models import Equipo

class EquipoAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["name"]}

admin.site.register(Equipo, EquipoAdmin)
