from django.contrib import admin
from .models import Equipo
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class EquipoResource(resources.ModelResource):
    class Meta:
        model = Equipo

class EquipoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug":["name"]}
    resource_class = EquipoResource

admin.site.register(Equipo, EquipoAdmin)
