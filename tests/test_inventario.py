import pytest
from src.inventario import clasificar_stock, calcular_porcentaje

def test_stock_agotado():
	assert clasificar_stock(0, 20) == "AGOTADO"

def test_stock_critico():
	assert clasificar_stock(7, 20) == "CRITICO"

def test_stock_bajo():
	assert clasificar_stock(15, 20) == "BAJO"

def test_stock_normal():
	assert clasificar_stock(30, 20) == "NORMAL"

def sobrestock():
	assert clasificar_stock(150, 20) == "SOBRESTOCK"

def stock_invalido():
	with pytest.raises(ValueError):
		clasificar_stock(-2, 20)

def test_calcular_porcentaje_normal():
    assert calcular_porcentaje(30, 100) == 30.0
    assert calcular_porcentaje(450, 600) == 75.0

def test_calcular_porcentaje_con_decimales():
    assert calcular_porcentaje(1, 3) == pytest.approx(33.333, abs=1e-3)

def test_calcular_porcentaje_limites():
    assert calcular_porcentaje(0, 100) == 0.0
    assert calcular_porcentaje(100, 100) == 100.0

def test_calcular_porcentaje_sobrestock():
    assert calcular_porcentaje(150, 100) == 150.0

def test_calcular_porcentaje_division_por_cero():
    with pytest.raises(ZeroDivisionError):
        calcular_porcentaje(50, 0)

def test_calcular_porcentaje_valores_negativos():
    with pytest.raises(ValueError):
        calcular_porcentaje(-10, 100)

