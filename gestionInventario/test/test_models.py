import pytest
from django.contrib.auth.models import User
from gestionInventario.models import Producto, Categoria
from datetime import datetime


# Crear usuario para las pruebas
@pytest.fixture
def usuario():
    return User.objects.create_user(username="testuser", password="testpassword")


# Crear categoría para las pruebas
@pytest.fixture
def categoria():
    return Categoria.objects.create(nombre="Electrónica", descripcion="Productos electrónicos")


# 1. Prueba del modelo Categoria
@pytest.mark.django_db
def test_categoria(categoria):
    # Verificar que el objeto categoría se haya creado correctamente
    assert categoria.nombre == "Electrónica"
    assert categoria.descripcion == "Productos electrónicos"
    assert str(categoria) == categoria.nombre  # Verificar el método __str__()


# 2. Prueba del modelo Producto
@pytest.mark.django_db
def test_producto(usuario, categoria):
    # Crear un producto con un usuario y una categoría
    producto = Producto.objects.create(
        nombre="Producto Test",
        precio=100.00,
        descripcion="Descripción de prueba",
        cantidad=10,
        stock=5,
        categoria=categoria,
        ingresado_por=usuario,
        fecha=datetime.now(),
        imagen="imagen.jpg"
    )

    # Verificar que el producto se haya creado correctamente
    assert producto.nombre == "Producto Test"
    assert producto.precio == 100.00
    assert producto.descripcion == "Descripción de prueba"
    assert producto.cantidad == 10
    assert producto.stock == 5
    assert producto.categoria == categoria
    assert producto.ingresado_por == usuario
    assert producto.fecha is not None
    assert producto.imagen == "imagen.jpg"
    assert str(producto) == producto.nombre  # Verificar el método __str__()


# 3. Prueba de validación del campo precio
@pytest.mark.django_db
def test_precio_producto_valido(usuario, categoria):
    # Crear un producto con un precio válido
    producto = Producto.objects.create(
        nombre="Producto Válido",
        precio=200.00,
        descripcion="Producto con precio válido",
        cantidad=5,
        stock=5,
        categoria=categoria,
        ingresado_por=usuario,
        fecha=datetime.now(),
        imagen="imagen_valida.jpg"
    )

    assert producto.precio == 200.00


# 4. Prueba de validación de cantidad y stock
@pytest.mark.django_db
def test_stock_producto(usuario, categoria):
    # Crear un producto con cantidad y stock
    producto = Producto.objects.create(
        nombre="Producto Stock Test",
        precio=50.00,
        descripcion="Producto para probar stock y cantidad",
        cantidad=15,
        stock=10,
        categoria=categoria,
        ingresado_por=usuario,
        fecha=datetime.now(),
        imagen="imagen_stock.jpg"
    )

    assert producto.cantidad == 15
    assert producto.stock == 10


# 5. Prueba para verificar el valor predeterminado del campo imagen
@pytest.mark.django_db
def test_imagen_predeterminada(usuario, categoria):
    # Crear un producto sin especificar la imagen
    producto = Producto.objects.create(
        nombre="Producto sin imagen",
        precio=80.00,
        descripcion="Producto sin imagen especificada",
        cantidad=5,
        stock=5,
        categoria=categoria,
        ingresado_por=usuario,
        fecha=datetime.now()
    )

    # Verificar que el campo imagen tenga el valor predeterminado
    assert producto.imagen == ''
