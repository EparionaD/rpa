# Generated by Django 3.2.3 on 2021-05-29 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catedra', '0009_alter_catedra_date_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catedra',
            name='date_create',
            field=models.DateField(auto_now_add=True, verbose_name='Fecha de creación'),
        ),
    ]