# Generated by Django 4.1.7 on 2023-04-29 11:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeustubularSL_app', '0002_empleado_telfono'),
    ]

    operations = [
        migrations.AddField(
            model_name='proceso',
            name='fechaFin',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
        migrations.AddField(
            model_name='proceso',
            name='fechaIni',
            field=models.DateTimeField(default=datetime.datetime.today),
        ),
    ]