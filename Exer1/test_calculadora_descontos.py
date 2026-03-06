from calculadora_descontos import *
import pytest

def test_percentual_desconto_maior_100():
    with pytest.raises(ValueError):
        calcular_desconto(100, 110)

def test_percentual_desconto_menor_que_0():
    with pytest.raises(ValueError):
        calcular_desconto(100, -1)


def test_valor_menor_ou_igual_que_zero():
    with pytest.raises(ValueError):
        calcular_desconto(0, 10)

def test_valor_com_desconto_basico():
    assert calcular_desconto(100, 10) == 90

def test_desconto_maximo():
    assert calcular_desconto(100, 100) == 0

def test_sem_desconto():
    assert calcular_desconto(100, 0) == 100

def test_percentual_desconto_maior_valor_original():
    assert calcular_desconto(20, 80) == pytest.approx(4.0)