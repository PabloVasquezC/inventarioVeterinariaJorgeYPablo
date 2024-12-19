from pyexpat.errors import messages
from django.shortcuts import redirect, render
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Venta




def lista_ventas(request):
    
    ventas = Venta.objects.all()
    
    return render(request, 'ventas/sales.html', {'ventas': ventas})


def agregar_venta(request):
    if request.method == "POST":

        fecha = request.POST.get('fecha')
        total_venta = request.POST.get('total_venta')
        numero_boleta = request.POST.get('numero_boleta')
        # Guardar la venta en la base de datos
        Venta.objects.create(
            fecha=fecha,
            total_venta=total_venta,
            numero_boleta=numero_boleta,
        )
        return redirect('lista_ventas')

    return render(request, 'ventas/add_venta.html')

# def editar_producto(request, id):
#     producto = Producto.objects.get(id=id)
#     categorias = Categoria.objects.all()  # Obtén todas las categorías

#     if request.method == "POST":
#         producto.nombre = request.POST.get('nombre')
#         producto.descripcion = request.POST.get('descripcion')
#         producto.precio = request.POST.get('precio')
#         producto.imagen = request.POST.get('imagen')
#         producto.stock = request.POST.get('stock')
#         categoria_id = request.POST.get('categoria')
        
#         producto.save()
        

#         return redirect('lista_productos')

#     return render(request, 'productos/edit_product.html', {'producto': producto, 'categorias': categorias})

def editar_venta(request, id):
    venta = Venta.objects.get(id=id)

    if request.method == "POST":
        venta.fecha = request.POST.get('fecha')
        venta.total_venta = request.POST.get('total_venta')
        venta.numero_boleta = request.POST.get('numero_boleta')
        
        venta.save()
        return redirect('lista_productos')

    return render(request, 'ventas/edit_venta.html', {'venta': venta})


def eliminar_venta(request, id):
    venta = Venta.objects.get(id=id)
    venta.delete()
    return redirect('lista_ventas')
