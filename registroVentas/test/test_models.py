import pytest
from registroVentas.models import Venta
from datetime import datetime


# 1. Prueba del modelo Venta
@pytest.mark.django_db
def test_venta():
    # Crear una venta
    venta = Venta.objects.create(
        total_venta=1000.00,
        numero_boleta=12345
    )

    # Verificar que la venta se haya creado correctamente
    assert venta.total_venta == 1000.00
    assert venta.numero_boleta == 12345
    assert isinstance(venta.fecha, datetime)  # Verificar que 'fecha' es un objeto datetime
    assert str(venta) == str([venta.fecha, venta.total_venta, venta.numero_boleta])  # Verificar el método __str__()

# 2. Prueba de validación de total_venta
@pytest.mark.django_db
def test_total_venta_valido():
    # Crear una venta con un total de venta válido
    venta = Venta.objects.create(
        total_venta=500.50,
        numero_boleta=54321
    )

    assert venta.total_venta == 500.50

# 3. Prueba de validación de numero_boleta
@pytest.mark.django_db
def test_numero_boleta_valido():
    # Crear una venta con un número de boleta válido
    venta = Venta.objects.create(
        total_venta=250.00,
        numero_boleta=98765
    )

    assert venta.numero_boleta == 98765
