from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from apps.author.models import Author

class Actualidades(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=255, blank=False, null=False)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    date = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    summary = RichTextField('Resumen', blank=True, null=True)
    description = RichTextUploadingField('Descripción', blank=False, null=False)
    pdf = models.FileField('Archivo PDF', upload_to='acctualidades-pdf/', blank=True, null=True)
    photo = models.ImageField('Fotografía', upload_to='actualidades/')
    author = models.ForeignKey(Author, verbose_name="Autor", on_delete=models.CASCADE)
    state = models.BooleanField('Activo/No activo', default=True)
    date_create = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Actualidad'
        verbose_name_plural = 'Actualidades'
        ordering = ['-date_create']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Actualidades, self).save(*args, **kwargs)