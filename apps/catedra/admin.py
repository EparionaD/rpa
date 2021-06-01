from django.contrib import admin
from .models import Catedra, Categorias

class CategoriasAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["name"]}
    list_display = ('name','slug','state')

class CatedraAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":["title"]}
    list_display = ('title','categorias','state')

admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Catedra, CatedraAdmin)
