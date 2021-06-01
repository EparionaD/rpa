# Generated by Django 3.2.3 on 2021-05-31 02:25

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('bio', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Descripción')),
                ('photo', models.ImageField(upload_to='equipo/', verbose_name='Portada')),
                ('email', models.EmailField(blank=True, max_length=255, null=True, verbose_name='Correo electrónico')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter')),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True, verbose_name='Whatsapp')),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Linkedin')),
                ('state', models.BooleanField(default=True, verbose_name='Activo/No activo')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['-date_create'],
            },
        ),
    ]