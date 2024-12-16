import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from gestionInventario.models import Producto, Categoria

# Crear fixtures para usuarios y categorías
@pytest.fixture
def categoria():
    return Categoria.objects.create(nombre='Electrónica')

@pytest.fixture
def usuario():
    return User.objects.create_user(username='testuser', password='testpassword')

@pytest.fixture
def producto(categoria, usuario):
    return Producto.objects.create(
        nombre='Producto Test',
        descripcion='Descripción de prueba',
        precio=100,
        imagen='imagen.jpg',
        stock=10,
        categoria=categoria,
        ingresado_por=usuario
    )

# 1. Probar la vista de lista de productos
@pytest.mark.django_db
def test_lista_productos(usuario, categoria, producto, client):
    # Crear un usuario administrador (staff) para probar la vista
    usuario.is_staff = True
    usuario.save()

    # Iniciar sesión con el usuario administrador
    client.login(username='testuser', password='testpassword')

    # Realizar la solicitud GET a la vista
    response = client.get(reverse('lista_productos'))

    # Verificar que la respuesta sea correcta
    assert response.status_code == 200
    assert 'productos' in response.context
    assert len(response.context['productos']) > 0
    assert 'categorias' in response.context
    assert len(response.context['categorias']) > 0

# 2. Probar la vista de agregar producto
@pytest.mark.django_db
def test_agregar_producto(usuario, categoria, client):
    client.login(username='testuser', password='testpassword')

    # Realizar una solicitud POST para agregar un producto
    response = client.post(reverse('agregar_producto'), {
        'nombre': 'Nuevo Producto',
        'descripcion': 'Descripción del nuevo producto',
        'precio': 150,
        'imagen': 'imagen2.jpg',
        'stock': 20,
        'categoria': categoria.id
    })

    # Verificar que la respuesta sea un redireccionamiento a 'lista_productos'
    assert response.status_code == 302
    assert Producto.objects.count() == 2  # Asegurarse de que se haya creado un producto nuevo

# 3. Probar la vista de editar producto
@pytest.mark.django_db
def test_editar_producto(usuario, producto, categoria, client):
    client.login(username='testuser', password='testpassword')

    # Realizar una solicitud POST para editar el producto
    response = client.post(reverse('editar_producto', kwargs={'id': producto.id}), {
        'nombre': 'Producto Editado',
        'descripcion': 'Descripción editada',
        'precio': 200,
        'imagen': 'imagen_editada.jpg',
        'stock': 30,
        'categoria': categoria.id
    })

    # Verificar que el producto haya sido editado y redirigido
    producto.refresh_from_db()
    assert response.status_code == 302
    assert producto.nombre == 'Producto Editado'
    assert producto.descripcion == 'Descripción editada'
    assert producto.precio == 200

# 4. Probar la vista de eliminar producto
@pytest.mark.django_db
def test_eliminar_producto(usuario, producto, client):
    client.login(username='testuser', password='testpassword')

    # Realizar la solicitud GET para eliminar el producto
    response = client.get(reverse('eliminar_producto', kwargs={'id': producto.id}))

    # Verificar que el producto se haya eliminado
    assert response.status_code == 302
    assert Producto.objects.count() == 0
