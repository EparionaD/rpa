from django.db import models
from django.utils.text import slugify
from django.db.models.fields import DateField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Categoría', max_length=255, blank=False, null=False)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    state = models.BooleanField('Activo/No activo', default=True)
    date_create = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        ordering = ['-date_create']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Categorias, self).save(*args, **kwargs)

class Catedra(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=255, blank=False, null=False)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    description = RichTextUploadingField('Descripción', blank=False, null=False)
    photo = models.ImageField('Portada', upload_to='catedra/')
    date = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    duration = models.CharField('Duración', max_length=100)
    time = models.TimeField('Hora', auto_now=False, auto_now_add=False)
    categorias = models.ForeignKey(Categorias, verbose_name="Categoría", on_delete=models.CASCADE)
    state = models.BooleanField('Activo/No activo', default=True)
    date_create = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Catedra'
        verbose_name_plural = 'Catedras'
        ordering = ['-date_create']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Catedra, self).save(*args, **kwargs)