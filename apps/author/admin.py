from django.contrib import admin
from .models import Author
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class AuthorResource(resources.ModelResource):
    class Meta:
        model = Author

class AuthorAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = AuthorResource

admin.site.register(Author, AuthorAdmin)