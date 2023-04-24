from django.db import models
#en un equipo1 puede haber varios procesos n
#en un proceso1 varios empl n
class equipo (models.Model):
    nombre = models.CharField(max_length = 150)
    modelo = models.CharField(max_length = 150)
    fechaAdquisicion = models.DateField
    fechaInstalacion = models.DateField
    categoria = models.CharField(max_length = 150)
    def __str__(self):
        return self.nombre
    
class proceso (models.Model):
    nombre = models.CharField(max_length = 150)
    ordenFabricacion = models.Value
    codigoProceso = models.Value
    referencia = models.CharField(max_length=150)
    fechaIni = models.DateField
    fechaFin = models.DateField
    FKidEquipo = models.ForeignKey (equipo, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre
    
class empleado (models.Model):
    nombre = models.CharField(max_length = 150)
    apellidos = models.CharField(max_length = 150) 
    DNI = models.CharField(max_length = 150)
    email = models.CharField(max_length = 150)
    telfono = models.Value
    FKidProcesp = models.ForeignKey (proceso, on_delete = models.CASCADE)
    def __str__(self):
        return self.nombre

