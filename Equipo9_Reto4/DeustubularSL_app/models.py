from msilib.schema import ListView
from django.db import models
import datetime
#en un equipo1 puede haber varios procesos n
#en un proceso1 varios empl n
class equipo (models.Model):
    nombre = models.CharField(max_length = 150)
    modelo = models.CharField(max_length = 150)
    fechaAdquisicion = models.DateTimeField(default=datetime.datetime.today)
    fechaInstalacion = models.DateTimeField(default=datetime.datetime.today)
    categoria = models.CharField(max_length = 150)
    def __str__(self):
        return self.nombre
    
class proceso (models.Model):
    nombre = models.CharField(max_length = 150)
    ordenFabricacion = models.IntegerField(default=0)
    codigoProceso = models.IntegerField(default=0)
    referencia = models.CharField(max_length=150)
    fechaIni = models.DateTimeField(default=datetime.datetime.today)
    fechaFin = models.DateTimeField(default=datetime.datetime.today)
    FKidEquipo = models.ForeignKey (equipo, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre
    
class empleado (models.Model):
    nombre = models.CharField(max_length = 150)
    apellidos = models.CharField(max_length = 150) 
    DNI = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    telfono = models.IntegerField(max_length=9,default=0)
    FKidProcesp = models.ForeignKey (proceso, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre
    




 

