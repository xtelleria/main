from django import forms
from .models import equipo,empleado,proceso
from django.forms import ModelForm

#Aqui se crean los formularios para los modelos,se selecciona el modelo y para cada uno de ellos se cogen todos
#sus campos gracias a  "fields = '__all__'"
class FormNuevoEmpleado(ModelForm):
 class Meta:
  model = empleado
  fields = '__all__'

class FormNuevoEquipo(ModelForm):
 class Meta:
  model = equipo
  fields = '__all__'

class FormNuevoProceso(ModelForm):
 class Meta:
  model = proceso
  fields = '__all__'







