# Generated by Django 3.2.3 on 2021-06-09 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0002_alter_publicaciones_summary'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='publicaciones',
            options={'ordering': ['-date_create'], 'verbose_name': 'Publicación', 'verbose_name_plural': 'Publicaciones'},
        ),
    ]
