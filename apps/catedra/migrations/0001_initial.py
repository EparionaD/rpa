# Generated by Django 3.2.3 on 2021-05-29 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Categoría')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='Slug')),
                ('state', models.BooleanField(default=True, verbose_name='Activo/No activo')),
                ('date_create', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Catedra',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255, verbose_name='Título')),
                ('slug', models.SlugField(editable=False, max_length=255, unique=True, verbose_name='Slug')),
                ('description', models.TextField(max_length=255, verbose_name='Descripción')),
                ('photo', models.ImageField(upload_to='catedra/', verbose_name='Portada')),
                ('date', models.DateField(verbose_name='Fecha')),
                ('duration', models.CharField(max_length=100, verbose_name='Duración')),
                ('time', models.TimeField(verbose_name='Hora')),
                ('state', models.BooleanField(default=True, verbose_name='Activo/No activo')),
                ('date_create', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
                ('categorias', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catedra.categorias', verbose_name='Categoría')),
            ],
            options={
                'verbose_name': 'Catedra',
                'verbose_name_plural': 'Catedras',
                'ordering': ['title'],
            },
        ),
    ]
