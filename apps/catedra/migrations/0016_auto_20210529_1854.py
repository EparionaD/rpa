# Generated by Django 3.2.3 on 2021-05-29 23:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catedra', '0015_alter_categorias_date_create'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catedra',
            options={'ordering': ['-date_create'], 'verbose_name': 'Catedra', 'verbose_name_plural': 'Catedras'},
        ),
        migrations.AlterModelOptions(
            name='categorias',
            options={'ordering': ['-date_create'], 'verbose_name': 'Categoría', 'verbose_name_plural': 'Categorías'},
        ),
        migrations.AlterField(
            model_name='catedra',
            name='date_create',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]
