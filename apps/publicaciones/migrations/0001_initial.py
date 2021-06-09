# Generated by Django 3.2.3 on 2021-06-05 21:29

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0002_alter_author_date_create'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Categoría')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('state', models.BooleanField(default=True, verbose_name='Activo/No activo')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['-date_create'],
            },
        ),
        migrations.CreateModel(
            name='Publicaciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('summary', models.CharField(max_length=255, verbose_name='Resumen')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Descripción')),
                ('photo', models.ImageField(upload_to='publicaciones/', verbose_name='Fotografía')),
                ('pdf', models.FileField(upload_to='pdf/', verbose_name='Archivo PDF')),
                ('facebook', models.CharField(blank=True, max_length=255, null=True, verbose_name='Facebook')),
                ('twitter', models.CharField(blank=True, max_length=255, null=True, verbose_name='Twitter')),
                ('whatsapp', models.CharField(blank=True, max_length=255, null=True, verbose_name='Whatsapp')),
                ('linkedin', models.CharField(blank=True, max_length=255, null=True, verbose_name='Linkedin')),
                ('state', models.BooleanField(default=True, verbose_name='Activo/No activo')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.author', verbose_name='Autor')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='publicaciones.categorias', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Publicación',
                'verbose_name_plural': 'Publicaciones',
                'ordering': ['date_create'],
            },
        ),
    ]