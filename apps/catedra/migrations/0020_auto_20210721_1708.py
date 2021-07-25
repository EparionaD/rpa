# Generated by Django 3.2.3 on 2021-07-21 22:08

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catedra', '0019_alter_catedra_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='catedra',
            name='cost',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Costo:'),
        ),
        migrations.AddField(
            model_name='catedra',
            name='guided',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Dirigido a:'),
        ),
        migrations.AddField(
            model_name='catedra',
            name='modality',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Modalidad:'),
        ),
        migrations.AddField(
            model_name='catedra',
            name='schedule',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Horario:'),
        ),
        migrations.AddField(
            model_name='catedra',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Resumen'),
        ),
        migrations.AlterField(
            model_name='catedra',
            name='date',
            field=models.DateField(verbose_name='Inicio'),
        ),
    ]