# Generated by Django 3.1.2 on 2020-11-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miapp', '0010_auto_20201107_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datosper',
            name='certificado',
            field=models.TextField(default='Prog. de microcomputadoras (ESPOL)'),
        ),
    ]
