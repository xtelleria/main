from django.urls import path,include
from . import views

urlpatterns = [
# Path para el index de la pagina
 path('', views.index, name='index'),
 # Paths para mostrar información
 path('1', views.listar_empleados, name='listar_empleados'),
 path('2', views.listar_procesos, name='listar_proceso'),
 path('4', views.listar_equipos, name='listar_equipos'),

# Paths para vistas detalladas
 path('5/<int:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
 path('3/<int:proceso_id>/', views.detalle_proceso, name='detalle_proceso'),

# Paths para crear nuevos objetos
 path('2/create', views.EmpleadoCreateView.as_view(), name='empleado_create'),
 path('3/create', views.EquipoCreateView.as_view(), name='equipo_create'),
 path('4/create', views.ProcesoCreateView.as_view(), name='proceso_create'),

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
]