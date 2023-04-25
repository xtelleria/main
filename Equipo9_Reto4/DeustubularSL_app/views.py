from django.shortcuts import render
from django.http import HttpResponse
from .models import equipo, proceso, empleado

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





