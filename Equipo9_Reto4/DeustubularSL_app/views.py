from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import equipo, empleado, proceso
from django.views import View
from django.views.generic import DetailView, ListView
from DeustubularSL_app.forms import LoginForm,FormNuevoEmpleado,FormNuevoEquipo,FormNuevoProceso


def index(request):
    return render(request,'DeustubularSL_app/index.html')

def mostrar_empleados(request, FKidProceso):
    empleados = empleado.objects.filter(FKidProcesp=FKidProceso)
    return render(request, 'DeustubularSL_app/empleado_mostrar.html', {'empleados': empleados})

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
    def post(self, request, *args, **kwargs):
        form = FormNuevoEmpleado(request.POST)
        if(form.is_valid()):
            empleados = empleado()
            empleados.nombre = form.cleaned_data['nombre']
            empleados.apellidos = form.cleaned_data['apellidos']
            empleados.DNI = form.cleaned_data['DNI']
            empleados.email = form.cleaned_data['email']
            empleados.telfono = form.cleaned_data['telfono']
            empleados.FKidProcesp = form.cleaned_data['FKidProcesp']
            empleados.save()
            return redirect('index')
        return render(request, 'empleado_create.html', {'form': form})
    
class EquipoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        formulario = FormNuevoEquipo()
        context = {
            'formulario': formulario
        }
        return render(request, 'DeustubularSL_app/equipo_create.html', context)
    def post(self, request, *args, **kwargs):
        form = FormNuevoEquipo(request.POST)
        if(form.is_valid()):
            equipos = equipo()
            equipos.nombre = form.cleaned_data['nombre']
            equipos.modelo = form.cleaned_data['modelo']
            equipos.fechaAdquisicion = form.cleaned_data['fechaAdquisicion']
            equipos.fechaInstalacion = form.cleaned_data['fechaInstalacion']
            equipos.categoria = form.cleaned_data['categoria']
            equipos.save()
            return redirect('aaaaaa')
        return render(request, 'equipo_create.html', {'form': form})
    
class ProcesoCreateView(View):
    # Llamada para mostrar la página con el formulario de creación al usuario
    def get(self, request, *args, **kwargs):
        formulario = FormNuevoProceso()
        context = {
            'formulario': formulario
        }
        return render(request, 'DeustubularSL_app/proceso_create.html', context)
    def post(self, request, *args, **kwargs):
        form = FormNuevoProceso(request.POST)
        if(form.is_valid()):
            procesos = proceso()
            procesos.nombre= form.cleaned_data['nombre']
            procesos.ordenFabricacion = form.cleaned_data['ordenFabricacion']
            procesos.codigoProceso = form.cleaned_data['codigoProceso']
            procesos.referencia = form.cleaned_data['referencia']
            procesos.fechaIni = form.cleaned_data['fechaIni']
            procesos.fechaFin = form.cleaned_data['fechaFin']
            procesos.FKidEquipo = form.cleaned_data['FKidEquipo']
            procesos.save()
            return redirect('bbbbb')
        return render(request, 'proceso_create.html', {'form': form})
    

def eliminar(request):
    return render(request, 'DeustubularSL_app/index_eliminar.html')








