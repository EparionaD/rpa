from django.db import models

class Firma(models.Model):
    title = models.CharField('Título', max_length=255, blank=False, null=False)
    summary = models.TextField('Descripción imagen de fondo', blank=True, null=True)
    image_background = models.ImageField('Imagen de fondo', upload_to='firma/',)
    description_founder = models.TextField('Descripción fundador', blank=True, null=True)
    partner = models.TextField('Descripción socio fundador', blank=True, null=True)
    image_partner = models.ImageField('Imagen de socio fundador', upload_to='firma/',)
    value_firma = models.TextField('Descripción de Valores', blank=True, null=True)
    responsibility_firma = models.TextField('Descripción de Responsabilidad social', blank=True, null=True)
    red_firma = models.TextField('Descripción de Red Internacional', blank=True, null=True)

    class Meta:
        verbose_name = 'Firma'
        verbose_name_plural = 'Firma'

    def __str__(self):
        return self.title