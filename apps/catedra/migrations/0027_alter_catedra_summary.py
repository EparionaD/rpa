# Generated by Django 3.2.3 on 2021-08-20 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catedra', '0026_auto_20210819_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catedra',
            name='summary',
            field=models.TextField(blank=True, null=True, verbose_name='Subtítulo'),
        ),
    ]
