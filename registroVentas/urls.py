from django.urls import path

from registroVentas.views import *

urlpatterns = [
    path('lista_ventas/', lista_ventas, name='lista_ventas'),
    path('agregar_venta/', agregar_venta, name='agregar_venta'),
    path('editar_venta/<int:id>/', editar_venta, name='editar_venta'),
    path('eliminar_venta/<int:id>/', eliminar_venta, name='eliminar_venta'),
]
