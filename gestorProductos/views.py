from django.shortcuts import render
from django.shortcuts import render
from .models import Producto

def lista_productos(request):
    productos = Producto.objects.all()  # Obtén todos los productos
    return render(request, 'productos/products.html', {'productos': productos})