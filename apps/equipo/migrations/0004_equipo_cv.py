# Generated by Django 3.2.3 on 2021-06-05 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0003_auto_20210601_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipo',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='cv/', verbose_name='Curriculum Vitae'),
        ),
    ]