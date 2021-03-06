# Generated by Django 3.2.3 on 2021-08-20 02:00

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catedra', '0025_auto_20210725_1323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catedra',
            name='photo',
            field=models.ImageField(upload_to='catedra/', verbose_name='Imagen de portada'),
        ),
        migrations.AlterField(
            model_name='catedra',
            name='summary',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Subtítulo'),
        ),
    ]
