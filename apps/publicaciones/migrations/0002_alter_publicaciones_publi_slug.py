# Generated by Django 3.2.3 on 2021-08-26 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicaciones',
            name='publi_slug',
            field=models.SlugField(max_length=255, verbose_name='Slug'),
        ),
    ]