from django.urls import path,include
from . import views
from .views import listar_equipos, listar_empleados, DetalleEmpleadoView

urlpatterns = [
# Path para el index de la pagina
 path('', views.index, name='index'),
 # Paths para mostrar información
 path('empleados', listar_empleados.as_view(), name='listar_empleados'),
 path('procesos', views.listar_procesos, name='listar_proceso'),
 path('equipos', listar_equipos.as_view(), name='listar_equipo'),
 # Paths para vistas detalladas
 path('empleados/detalle_empleado<int:pk>/', DetalleEmpleadoView.as_view(), name='detalle_empleado'),
 path('procesos/<int:proceso_id>/', views.detalle_proceso, name='detalle_proceso'),


# Paths para crear nuevos objetos
 path('empleados/create', views.EmpleadoCreateView.as_view(), name='empleado_create'),
 path('equipos/create', views.EquipoCreateView.as_view(), name='equipo_create'),
 path('procesos/create', views.ProcesoCreateView.as_view(), name='proceso_create'),

# Paths para mostrar una pagina principal de borrado en la cual se selecciona
# que se desea borrar empleados/procesos/equipos
 path('eliminar/', views.eliminar, name='eliminar'),

# Paths para borrar en especifico 
 path('eliminar/empleado', views.lista_empleados, name='lista_empleados'),
 path('eliminar/empleado/<int:id_empleado>/', views.eliminar_empleado, name='eliminar_empleado'),

 path('eliminar/proceso', views.lista_procesos, name='lista_procesos'),
 path('eliminar/proceso/<int:id_proceso>/', views.eliminar_proceso, name='eliminar_proceso'),

  path('eliminar/equipo', views.lista_equipos, name='lista_equipos'),
  path('eliminar/equipo/<int:id_equipo>/', views.eliminar_equipo, name='eliminar_equipo'),
# Paths para mostrar una pagina si alguno de los fields no es correcto
  path('errorEmail/', views.mostrar_mensajeEmail, name='errorEmail'),
  path('errorDni/', views.mostrar_mensajeDni, name='errorDni'),
  # Paths para mostrar el formulario para mandar el email
  path('enviar-correo/', views.enviar_correo, name='enviar_correo'),
  path('filtrar-empleados/', views.filtrar_empleados, name='filtrar_empleados'),
  path('filtrar-equipos/', views.filtrar_equipos, name='filtrar_equipos'),
  path('filtrar-procesos/', views.filtrar_procesos, name='filtrar_procesos'),
  path('api/datos/', views.datos_api, name='datos_api'),
]