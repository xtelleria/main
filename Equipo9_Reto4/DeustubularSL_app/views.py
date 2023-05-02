from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import equipo, empleado, proceso
from django.views import View
from django.shortcuts import redirect
from django.db.models import Count
from django.views.generic import DetailView, ListView
from DeustubularSL_app.forms import LoginForm,FormNuevoEmpleado,FormNuevoEquipo,FormNuevoProceso


def index(request):
    return render(request,'DeustubularSL_app/index.html')


def listar_empleados(request):
    empleados =  empleado.objects.all().order_by('FKidProcesp')
    context = {'empleados': empleados}
    return render(request, 'DeustubularSL_app/empleado_mostrar.html', context)

def listar_equipos(request):
    equipos = equipo.objects.all().order_by('nombre')
    return render(request, 'DeustubularSL_app/equipo_mostrar.html', {'equipos': equipos})

def listar_procesos(request):
    procesos = proceso.objects.annotate(num_empleados=Count('empleado'))
    return render(request, 'DeustubularSL_app/proceso_mostrar.html', {'procesos': procesos})

def detalle_proceso(request, proceso_id):
    procesos = get_object_or_404(proceso, pk=proceso_id)
    empleados = empleado.objects.order_by('FKidProcesp')
    context = {
        'proceso': procesos,
        'empleados' : empleados
    }
    return render(request, 'DeustubularSL_app/proceso_detalle.html', context)


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


def lista_empleados(request):
    empleados = empleado.objects.all()
    context = {'empleados': empleados}
    return render(request, 'DeustubularSL_app/lista_empleados_a_borrar.html', context)

def eliminar_empleado(request, id_empleado):
    empleados = get_object_or_404(empleado, id=id_empleado)
    empleados.delete()
    return redirect('lista_empleados')

def lista_procesos(request):
    procesos = proceso.objects.all()
    context = {'procesos': procesos}
    return render(request, 'DeustubularSL_app/lista_procesos_a_borrar.html', context)
def eliminar_proceso(request, id_proceso):
    procesos = get_object_or_404(proceso, id=id_proceso)
    procesos.delete()
    return redirect('lista_procesos')

def lista_equipos(request):
    equipos = equipo.objects.all()
    context = {'equipos': equipos}
    return render(request, 'DeustubularSL_app/lista_equipos_a_borrar.html', context)
def eliminar_equipo(request, id_equipo):
    equipos = get_object_or_404(proceso, id=id_equipo)
    equipos.delete()
    return redirect('lista_equipos')









