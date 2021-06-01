from django.db import models
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Nombres', max_length=255, blank=False, null=False)
    slug = models.SlugField('Slug', max_length=255, unique=True)
    grade = models.CharField('Grado académico', max_length=255, blank=True, null=True)
    bio = RichTextUploadingField('Biografía', blank=False, null=False)
    photo = models.ImageField('Fotografía', upload_to='equipo/')
    email = models.EmailField('Correo electrónico', max_length=255, blank=True, null=True)
    facebook = models.CharField('Facebook', max_length=255, blank=True, null=True)
    twitter = models.CharField('Twitter', max_length=255, blank=True, null=True)
    whatsapp = models.CharField('Whatsapp', max_length=255, blank=True, null=True)
    linkedin = models.CharField('Linkedin', max_length=255, blank=True, null=True)
    state = models.BooleanField('Activo/No activo', default=True)
    date_create = models.DateTimeField('Fecha de creación', auto_now_add=True)

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['date_create']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Equipo, self).save(*args, **kwargs)
