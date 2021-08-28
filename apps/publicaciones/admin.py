from django.contrib import admin
from .models import Categorias, Publicaciones
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriasResource(resources.ModelResource):
    class Meta:
        model = Categorias

class PublicacionesResource(resources.ModelResource):
    class Meta:
        model = Publicaciones

class CategoriasAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug":["name"]}
    resource_class = CategoriasResource

class PublicacionesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"publi_slug":["title"]}
    list_display = ('title','categorias','state')
    resource_class = PublicacionesResource

admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Publicaciones, PublicacionesAdmin)
