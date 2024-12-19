from django.urls import path
from gestionInventario.views import *
from generacionInformes.views import SignUpView
from generacionInformes.views import EditUserView



urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path('editar-perfil/', EditUserView.as_view(), name='edit_user'),
    path('lista_productos/', lista_productos, name='lista_productos'),
    path('agregar_producto/', agregar_producto, name='agregar_producto'),
    path('editar_producto/<int:id>/', editar_producto, name='editar_producto'),
    path('eliminar_producto/<int:id>/', eliminar_producto, name='eliminar_producto'),
    path('ventas', ventas, name='ventas')
]
