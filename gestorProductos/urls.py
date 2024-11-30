from django.urls import path

from gestorProductos.views import lista_productos

urlpatterns = [
    path('lista_productos/', lista_productos, name='lista_productos')
]
