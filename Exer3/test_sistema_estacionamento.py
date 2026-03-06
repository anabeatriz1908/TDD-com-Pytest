from sistema_estacionamento import *
import pytest

def test_40_minutos():
    assert calcular_valor_estacionamento(40) == 10

def test_60_minutos():
    assert calcular_valor_estacionamento(60) == 10

def test_70_minutos():
    assert calcular_valor_estacionamento(70) == 15

def test_90_minutos():
    assert calcular_valor_estacionamento(90) == 15

def test_180_minutos():
    assert calcular_valor_estacionamento(180) == 20

def test_24_horas():
    assert calcular_valor_estacionamento(1440) == 50
    
def test_tempo_negativo():
    with  pytest.raises(ValueError):
        calcular_valor_estacionamento(-50)

