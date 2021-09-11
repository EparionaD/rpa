from django.contrib import admin
from .models import Firma

class FirmaAdmin(admin.ModelAdmin):
    list_display = ('title',)

admin.site.register(Firma, FirmaAdmin)
