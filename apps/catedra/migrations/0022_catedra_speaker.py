# Generated by Django 3.2.3 on 2021-07-21 23:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catedra', '0021_catedra_contact_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='catedra',
            name='speaker',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Ponente:'),
        ),
    ]
