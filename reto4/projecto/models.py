from django.db import models

# Create your models here.
class Empleado(models.Model):
    dni = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
