from django.contrib import admin
from .models import Catedra, Categorias
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categorias

class CatedraResource(resources.ModelResource):
    class Meta:
        model = Catedra

class CategoriasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug":["name"]}
    list_display = ('name','slug','state')
    resource_class = CategoriaResource

class CatedraAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug":["title"]}
    list_display = ('title','categorias','state')
    resource_class = CatedraResource

admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Catedra, CatedraAdmin)
