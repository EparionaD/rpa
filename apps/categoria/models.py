from django.db import models

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Categoría', max_length=255, blank=False, null=False)
    state = models.BooleanField('Activo/No activo', default=True)
    date_create = models.DateField('Fecha de creación', auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['name']

    def __str__(self):
        return self.name