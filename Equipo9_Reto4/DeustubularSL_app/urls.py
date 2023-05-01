from django.urls import path,include
from . import views

urlpatterns = [
 path('', views.index, name='index'),
 #path('1', views.index_empleado, name='aaaaaa'),
 path('2', views.index_equipo, name='aaaaaa'),
 path('1/<int:FKidProceso>', views.mostrar_empleados, name='mostrar_empleados'),
 path('3', views.index_proceso, name='bbbbb'),
 #path('3', views.loginformEquipo, name='index'),
 #path('4', views.loginformEmpleado, name='index'),
# path('5', views.loginformProceso, name='index'),

     # Paths para crear
 path('2/create', views.EmpleadoCreateView.as_view(), name='empleado_create'),
 path('3/create', views.EquipoCreateView.as_view(), name='equipo_create'),
 path('4/create', views.ProcesoCreateView.as_view(), name='proceso_create'),

 path('eliminar/', views.eliminar, name='eliminar'),
#path('eliminarEmpleado/', views.eliminarEmpleado.as_view(), name='eliminarEmpleado'),
 
]