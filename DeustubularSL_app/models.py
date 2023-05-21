from msilib.schema import ListView
from django.db import models
import datetime
#Modelos para la aplicación de DeustubularSL, en este caso se ha conseiderado que un mismo
#equipo controla/monitorea varios procesos, y que en un proceso hay varios empleados.
class Categoria(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
    
class Referencia(models.Model):
    nombre = models.CharField(max_length=150)

    def __str__(self):
        return self.nombre
class equipo (models.Model):
    nombre = models.CharField(max_length = 150)
    modelo = models.CharField(max_length = 150)
    fechaAdquisicion = models.DateTimeField(default=datetime.datetime.today)
    fechaInstalacion = models.DateTimeField(default=datetime.datetime.today)
    #fechaAdquisicion = models.DateField(default=datetime.today)
    #fechaInstalacion = models.DateField(default=datetime.today)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class proceso (models.Model):
    nombre = models.CharField(max_length = 150)
    ordenFabricacion = models.IntegerField(default=0)
    codigoProceso = models.IntegerField(default=0)
    referencia = models.ForeignKey(Referencia, on_delete=models.CASCADE)
    fechaIni = models.DateTimeField(default=datetime.datetime.today)
    fechaFin = models.DateTimeField(default=datetime.datetime.today)
   # fechaIni = models.DateField(default=datetime.today)
    #fechaFin = models.DateField(default=datetime.today)
    FKidEquipo = models.ForeignKey (equipo, on_delete = models.CASCADE, related_name='procesos')
    def __str__(self):
        return self.nombre
    
class empleado (models.Model):
    nombre = models.CharField(max_length = 150)
    apellidos = models.CharField(max_length = 150) 
    DNI = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    telfono = models.IntegerField (max_length=9,default=0)
    FKidProcesp = models.ForeignKey (proceso, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre
    




 

