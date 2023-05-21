# Generated by Django 4.1.7 on 2023-05-20 11:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeustubularSL_app', '0005_proceso_codigoproceso_proceso_ordenfabricacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='telfono',
        ),
        migrations.AlterField(
            model_name='equipo',
            name='fechaAdquisicion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='equipo',
            name='fechaInstalacion',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='fechaFin',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='proceso',
            name='fechaIni',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
