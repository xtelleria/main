# Generated by Django 4.1.7 on 2023-05-20 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DeustubularSL_app', '0006_remove_empleado_telfono_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='telfono',
            field=models.IntegerField(default=0, max_length=9),
        ),
    ]
