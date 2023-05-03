from django.http import HttpResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render, redirect
from .models import equipo, empleado, proceso
from django.views import View
from django.shortcuts import redirect
from django.db.models import Count
from django.views.generic import DetailView, ListView
from DeustubularSL_app.forms import FormNuevoEmpleado,FormNuevoEquipo,FormNuevoProceso
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

#Métodos para la app

#Método index, se dedica a reenviar al usuario al html que muestra la pagina de inicio
def index(request):
    return render(request,'DeustubularSL_app/index.html')

#Método listar_empleados, se dedica a extraer todos los empleados ordenados por 
#el nombre de el proceso en ascendente,los guarda (en context) y despues redirecciona a la  pagina html correspondiente
#para poder mostrarlos
def listar_empleados(request):
    empleados =  empleado.objects.all().order_by('FKidProcesp')
    context = {'empleados': empleados}
    return render(request, 'DeustubularSL_app/empleado_mostrar.html', context)

#Lo mismo que empleados pero para equipo, en este caso se ordenan por el nombre de el equipo en ascendente
def listar_equipos(request):
    equipos = equipo.objects.all().order_by('nombre')
    context = {'equipos': equipos}
    return render(request, 'DeustubularSL_app/equipo_mostrar.html', context)

#Método para contar los empleados asociados a un proceso, luego carga una plantilla
#que muestra Nombre Proceso -- Num empleados, cuando el usuario clicka en un 
#proceso en concreto se le mostrara los detalles de el mismo
def listar_procesos(request):
    procesos = proceso.objects.annotate(num_empleados=Count('empleado'))
    context = {'procesos': procesos}
    return render(request, 'DeustubularSL_app/proceso_mostrar.html', context)

#Método que muestra los detalles de unu proceso segun su id
def detalle_proceso(request, proceso_id):
    procesos = get_object_or_404(proceso, pk=proceso_id)
    empleados = empleado.objects.order_by('FKidProcesp')
    context = {
        'proceso': procesos,
        'empleados' : empleados
    }
    return render(request, 'DeustubularSL_app/proceso_detalle.html', context)


#Métodos para mostrar un forulario para la creacion de distintos objetos
#En todos estos métodos hay dos apartados, cuando la petición es get; Muestra el formulario
#con los campos a rellenar, y post para alamacenar esos datos
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
            return redirect('listar_empleados')
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
            return redirect('listar_equipos')
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
            return redirect('listar_proceso')
        return render(request, 'proceso_create.html', {'form': form})
    
#Método que se utiliza para mostrar una pagina de inicio para eliminar objetos,
#primero muestra los tres modelos principales y despues se podra seleccionar
#uno de ellos para borrarlo
def eliminar(request):
    return render(request, 'DeustubularSL_app/index_eliminar.html')

#A la hora de borrar, para todos los casos se muestra primero una lista con los objetos
#y al hacer click en el boton "Eliminar" llamara a la funcion dedicada a eliminar, en todos 
#los casos se hace por el id de el objeto
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
    equipos = get_object_or_404(equipo, id=id_equipo)
    equipos.delete()
    return redirect('lista_equipos')









