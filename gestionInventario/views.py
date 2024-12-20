from django.shortcuts import render, redirect

# Create your views here.
from .models import Producto, Categoria

def lista_productos(request):
    if request.user.is_staff:
        productos = Producto.objects.all()
    else:
        productos = Producto.objects.filter(ingresado_por=request.user)
    
    categorias = Categoria.objects.all()

    return render(request, 'productos/products.html', {'productos': productos, 'categorias': categorias})

def agregar_producto(request):
    categorias = Categoria.objects.all()  # Obtén todas las categorías

    if request.method == "POST":
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        precio = request.POST.get('precio')
        imagen = request.POST.get('imagen')
        stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')

        categoria = Categoria.objects.get(id=categoria_id)  # Obtén la categoría seleccionada

        # Guardar el producto en la base de datos
        Producto.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            precio=precio,
            imagen=imagen,
            stock=stock,
            categoria=categoria,
            ingresado_por=request.user
        )
        return redirect('lista_productos')

    return render(request, 'productos/add_product.html', {'categorias': categorias})


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

def editar_producto(request, id):
    producto = Producto.objects.get(id=id)
    categorias = Categoria.objects.all()  # Obtén todas las categorías

    if request.method == "POST":
        producto.nombre = request.POST.get('nombre')
        producto.descripcion = request.POST.get('descripcion')
        producto.precio = request.POST.get('precio')
        producto.imagen = request.POST.get('imagen')
        producto.stock = request.POST.get('stock')
        categoria_id = request.POST.get('categoria')
        
        # Asignar la nueva categoría seleccionada
        producto.categoria = Categoria.objects.get(id=categoria_id)

        producto.save()
        return redirect('lista_productos')

    return render(request, 'productos/edit_product.html', {'producto': producto, 'categorias': categorias})



def eliminar_producto(request, id):
    producto = Producto.objects.get(id=id)
    producto.delete()
    return redirect('lista_productos')

