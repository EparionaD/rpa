# Generated by Django 3.2.3 on 2021-05-28 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255, verbose_name='Nombre')),
                ('last_name', models.CharField(max_length=255, verbose_name='Apellidos')),
                ('email', models.EmailField(max_length=255, verbose_name='Correo electrónico')),
                ('photo', models.ImageField(upload_to='autor/', verbose_name='Imagen de perfil')),
                ('state', models.BooleanField(default=True, verbose_name='Activo/No activo')),
                ('date_create', models.DateField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Autor',
                'verbose_name_plural': 'Autores',
                'ordering': ['name'],
            },
        ),
    ]
