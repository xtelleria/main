from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import equipo, empleado, proceso
from django.views import View
from django.views.generic import DetailView, ListView
from DeustubularSL_app.forms import LoginForm,FormNuevoEmpleado,FormNuevoEquipo,FormNuevoProceso


def index_empleado(request):
	empleados = empleado.objects.order_by('nombre')
	output = ', '.join([e.nombre for e in empleados])
	return HttpResponse(output)

def index_equipo(request):
	equipos = equipo.objects.order_by("nombre")
	output = ', '.join([eq.nombre for eq in equipos])
	return HttpResponse(output)

def index_proceso(request):
	
	procesos = proceso.objects.order_by('nombre')
	output = ', '.join([p.nombre for p in procesos])
	return HttpResponse(output)

def loginformEquipo(request):
 form = LoginForm()
 return render(
 request, 'login.html', {'form':form}
 )
class EmpleadoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        formulario = FormNuevoEmpleado()
        context = {
            'formulario': formulario
        }
        return render(request, 'DeustubularSL_app/empleado_create.html', context)
    
class EquipoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        formulario = FormNuevoEquipo()
        context = {
            'formulario': formulario
        }
        return render(request, 'DeustubularSL_app/equipo_create.html', context)
    
class ProcesoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        formulario = FormNuevoProceso()
        context = {
            'formulario': formulario
        }
        return render(request, 'DeustubularSL_app/proceso_create.html', context)




def loginformEmpleado(request):
 form = LoginForm()
 return render(
 request, 'login.html', {'form':form}
 )

def loginformProceso(request):
 form = LoginForm()
 return render(
 request, 'login.html', {'form':form}
 )
def show_FormEquipo(request):
     return render(request, "login.html")








