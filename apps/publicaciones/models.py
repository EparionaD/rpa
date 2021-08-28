from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from apps.author.models import Author

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

class Publicaciones(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Título', max_length=255, blank=False, null=False)
    publi_slug = models.SlugField('Slug', max_length=255, unique=False)
    date = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    summary = models.TextField('Subtítulo', blank=True, null=True)
    description = RichTextUploadingField('Contenido', blank=False, null=False)
    photo = models.ImageField('Imagen de publicación', upload_to='publicaciones/')
    pdf = models.FileField('Archivo PDF', upload_to='pdf/', blank=False, null=False)
    categorias = models.ForeignKey(Categorias, verbose_name="Categoría", on_delete=models.CASCADE)
    author = models.ForeignKey(Author, verbose_name="Autor", on_delete=models.CASCADE)
    # facebook = models.CharField('Facebook', max_length=255, blank=True, null=True)
    # twitter = models.CharField('Twitter', max_length=255, blank=True, null=True)
    # whatsapp = models.CharField('Whatsapp', max_length=255, blank=True, null=True)
    # linkedin = models.CharField('Linkedin', max_length=255, blank=True, null=True)
    state = models.BooleanField('Activo/No activo', default=True)
    date_create = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Publicación'
        verbose_name_plural = 'Publicaciones'
        ordering = ['-date_create']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Publicaciones, self).save(*args, **kwargs)