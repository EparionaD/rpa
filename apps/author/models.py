from django.db import models

class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombre', max_length=255, blank=False, null=False)
    last_name = models.CharField('Apellidos',max_length=255, blank=False, null=False)
    email = models.EmailField('Correo electrónico', max_length=255)
    photo = models.ImageField('Imagen de perfil', upload_to='autor/')
    state = models.BooleanField('Activo/No activo', default=True)
    date_create = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'
        ordering = ['name']

    def __str__(self):
        return self.name