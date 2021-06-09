from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Actualidades


class ActualidadesResource(resources.ModelResource):
    class Meta:
        model = Actualidades

class ActualidadesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    prepopulated_fields = {"slug":["title"]}
    list_display = ('title','state')
    resource_class = ActualidadesResource

admin.site.register(Actualidades, ActualidadesAdmin)
