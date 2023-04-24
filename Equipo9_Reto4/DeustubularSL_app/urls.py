from django.urls import path
from . import views

urlpatterns = [
 path('', views.index_empleado, name='index'),
 path('1', views.index_equipo, name='aaaaaa'),
 path('2', views.index_proceso, name='bbbbb'),
]