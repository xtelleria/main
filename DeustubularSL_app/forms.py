from django import forms
from .models import equipo,empleado,proceso
from django.forms import ModelForm
from django.core.validators import validate_email 

#Aqui se crean los formularios para los modelos,se selecciona el modelo y para cada uno de ellos se cogen todos
#sus campos gracias a  "fields = '__all__'"
class FormNuevoEmpleado(ModelForm):
 class Meta:
  model = empleado
  fields = '__all__'
  labels = {
            'FKidProcesp': 'Proceso Asociado',
            'telfono': 'Telefono',
        }


class FormNuevoEquipo(ModelForm):
 class Meta:
  model = equipo
  fields = '__all__'
  labels = {
            'fechaAdquisicion': 'Adquisición',
            'fechaInstalacion': 'Instalación'

        }

class FormNuevoProceso(ModelForm):
 class Meta:
  model = proceso
  fields = '__all__'
  labels = {
            'ordenFabricacion': 'Orden de Fabricacion',
            'codigoProceso': 'Codigo Procseso',
            'fechaIni': 'Fecha de inicio',
            'fechaFin': 'Fecha Fin',
            'FKidEquipo': 'Equipo',

        }







