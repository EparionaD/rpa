# Generated by Django 3.2.3 on 2021-05-30 21:57

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catedra', '0017_alter_catedra_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catedra',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=255, verbose_name='Descripción'),
        ),
    ]