from django import forms
from .models import equipo,empleado,proceso
from django.forms import ModelForm


class LoginForm(forms.Form):
 nombreEquipo = forms.CharField(label='nombreEquipo', max_length=100)
 modeloEquipo = forms.EmailField(label='modeloEquipo', max_length=20)
 fechaAdquisicionEquipo = forms.EmailField(label='fechaAdquisicionEquipo', max_length=20)
 fechaInstalacionEquipo = forms.EmailField(label='fechaInstalacionEquipo', max_length=20)
 categoriaEquipo = forms.EmailField(label='categoriaEquipo', max_length=20)

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







