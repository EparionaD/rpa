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
    summary = models.TextField('Subtítulo', blank=True, null=True)
    description = RichTextUploadingField('Descripción', blank=False, null=False)
    photo = models.ImageField('Imagen de portada', upload_to='catedra/')
    date = models.DateField('Inicio', auto_now=False, auto_now_add=False)
    duration = models.CharField('Duración', max_length=100)
    guided = models.CharField('Dirigido a:', max_length=150, blank=True, null=True)
    modality = models.CharField('Modalidad:', max_length=50, blank=True, null=True)
    schedule = models.CharField('Horario:', max_length=50, blank=True, null=True)
    cost = models.CharField('Costo:', max_length=50, blank=True, null=True)
    contact_number = models.CharField('Escribemos:', max_length=50, blank=True, null=True)
    syllabus = RichTextUploadingField('Plan de estudios', blank=True, null=True)
    # speaker = RichTextUploadingField('Docentes:', blank=True, null=True)
    profit = RichTextUploadingField('Beneficios:', blank=True, null=True)
    cathedra = RichTextUploadingField('El enfoque de aprendizaje de Cátedra:', blank=True, null=True)
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

class Speaker(models.Model):
    catedra = models.ForeignKey(Catedra, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField('Docente', max_length=150, blank=True, null=True)
    description = RichTextUploadingField('Descripción', blank=True, null=True)
    image = models.ImageField('Portada', upload_to='foto-ponente/', blank=True, null=True)

    class Meta:
        verbose_name = "Datos del docente"
        verbose_name_plural = "Datos de los docentes"