# Generated by Django 3.2.3 on 2021-08-20 02:00

import ckeditor.fields
import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actualidades', '0002_auto_20210725_1805'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actualidades',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='actualidades',
            name='summary',
            field=ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Subtítulo'),
        ),
    ]
