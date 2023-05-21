from django.contrib import admin
from .models import equipo, empleado, proceso, Categoria, Referencia
#Aquí se permite que al entrar como adminstrador pueda crear/eliminar datos
admin.site.register(equipo)
admin.site.register(empleado)
admin.site.register(proceso)
admin.site.register(Categoria)
admin.site.register(Referencia)