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
from django.core.mail import send_mail
from .forms import EmailForm
import re

#Métodos para la app

#Método index, se dedica a reenviar al usuario al html que muestra la pagina de inicio
def index(request):
    return render(request,'DeustubularSL_app/index.html')

#Método listar_empleados, se dedica a extraer todos los empleados ordenados por 
#el nombre de el proceso en ascendente,los guarda (en context) y despues redirecciona a la  pagina html correspondiente
#para poder mostrarlos
class listar_empleados(ListView):
    model= empleado
    template_name= 'DeustubularSL_app/empleado_mostrar.html'
    context_object_name = 'empleados'

#Método detalle_empleado para mostrar todos los valores de los atributos de un empleado en 
#especifico esto se hace gracias a su id
class DetalleEmpleadoView(DetailView):
    model = empleado
    template_name = 'DeustubularSL_app/empleado_detalle.html'
    context_object_name = 'empleado'

#Lo mismo que empleados pero para equipo, en este caso se ordenan por el nombre de el equipo en ascendente

class listar_equipos(ListView):
    model = equipo
    template_name = 'DeustubularSL_app/equipo_mostrar.html'
    context_object_name = 'equipos'

def detalle_equipo(request, equipo_id):
    equipos = get_object_or_404(equipo, id=equipo_id)
    context = {'equipos': equipos}
    return render(request, 'DeustubularSL_app/equipo_detalle.html', context)


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
class DetalleProcesoView(DetailView):
    model = proceso
    template_name = 'DeustubularSL_app/proceso_detalle.html'
    context_object_name = 'proceso'

def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        empleados = empleado.objects.order_by('FKidProcesp')
        context['empleados'] = empleados
        return context

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
            #if(comprobar_email(empleados.email) and comprobar_DNI(empleados.DNI)):
            empleados.save()
            #elif not(comprobar_DNI(empleados.DNI)):
             #   return redirect('errorDni')
            #elif not(comprobar_email(empleados.email)):
             #   return redirect('errorEmail')
            return redirect('listar_empleados')
        return render(request, 'DeustubularSL_app/empleado_create.html', {'form': form})
    
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
            return redirect('listar_equipo')
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

def lista_equipos(request):
    equipos = equipo.objects.all()
    context = {'equipos': equipos}
    return render(request, 'DeustubularSL_app/lista_equipos_a_borrar.html', context)
def eliminar_equipo(request, id_equipo):
    equipos = get_object_or_404(equipo, id=id_equipo)
    equipos.delete()
    return redirect('lista_equipos')



def lista_procesos(request):
    procesos = proceso.objects.all()
    context = {'procesos': procesos}
    return render(request, 'DeustubularSL_app/lista_procesos_a_borrar.html', context)
def eliminar_proceso(request, id_proceso):
    procesos = get_object_or_404(proceso, id=id_proceso)
    procesos.delete()
    return redirect('lista_procesos')




#Métodos para comprobar si el dni y el correo es correcto
def comprobar_email(email):
    dominios_validos = ["@deustubular.es", "@deusto.es"]
    for dominio in dominios_validos :
        if email.endswith(dominio):
            return True
    else : return False
def comprobar_DNI(dni):
   if re.match(r'\d{8}[a-zA-Z]$', dni):
       empleados = empleado.objects.all()
       print(empleados)
       for comprobar in empleados:
         if (comprobar.DNI ==  dni):
             print(comprobar.DNI)
             return False
        
       return True
   else :
       return False

#Métodos para cargar la pagina correspondiente para mosttrar el error
def mostrar_mensajeEmail(request):
     return render(request, 'DeustubularSL_app/no_valido_email.html')

def mostrar_mensajeDni(request):
     return render(request, 'DeustubularSL_app/no_valido_dni.html')

def mostrar_enviarCorreo(request):
    return render(request, 'DeustubularSL_app/enviar_Email.html')

def enviar_correo(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            asunto = form.cleaned_data['asunto']
            cuerpo = form.cleaned_data['cuerpo']
            remitente = form.cleaned_data['remitente']
            destinatario = form.cleaned_data['destinatario']
            
            send_mail(asunto, cuerpo, remitente, [destinatario])
            return render(request, 'DeustubularSL_app/enviado.html')
    else:
            form = EmailForm()
            return render(request, 'DeustubularSL_app/enviar_Email.html', {'form': form})

def filtrar_empleados(request):
    nombre = request.GET.get('nombre')
    dni = request.GET.get('dni')

    empleados = empleado.objects.all()

    if nombre:
        empleados = empleados.filter(nombre__icontains=nombre)
    if dni:
        empleados = empleados.filter(DNI=dni)

    return render(request, 'DeustubularSL_app/empleado_mostrar.html', {'empleados': empleados})

def filtrar_equipos(request):
    nombre = request.GET.get('nombre')
    modelo = request.GET.get('modelo')

    equipos = equipo.objects.all()

    if nombre:
        equipos = equipos.filter(nombre__icontains=nombre)
    if modelo:
        equipos = equipos.filter(modelo=modelo)

    return render(request, 'DeustubularSL_app/equipo_mostrar.html', {'equipos': equipos})

def filtrar_procesos(request):
    nombre = request.GET.get('nombre')
    num_empleados = request.GET.get('num_empleados')

    procesos = proceso.objects.all()

    if nombre:
        procesos = procesos.filter(nombre__icontains=nombre)
    if num_empleados:
        procesos = procesos.filter(num_empleados=num_empleados)

    return render(request, 'DeustubularSL_app/proceso_mostrar.html', {'procesos': procesos})



