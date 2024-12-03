from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Producto
from .models import Categoria


def lista_productos(request):
    if request.user.is_staff:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(created_by=request.user)
    
    categorias = Categoria.objects.all()

    return render(request, 'productos/products.html', {'productos': productos, 'categorias': categorias})

def agregar_producto(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        imagen = request.POST.get('imagen')
        stock = request.POST.get('stock')
        

        # Guardar el producto en la base de datos
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen,
            stock=stock,
            created_by=request.user
        )
        # Mensaje de éxito
        return redirect('lista_productos')  # Redirige al listado de productos

    return render(request, 'productos/add_product.html')

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    if request.method == "POST":
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.imagen = request.POST.get('imagen')
        producto.stock = request.POST.get('stock')
        producto.save()
        return redirect('lista_productos')

    return render(request, 'productos/add_product.html', {'producto': producto})


def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('lista_productos')

