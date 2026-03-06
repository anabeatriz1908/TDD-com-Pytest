import pytest
from conversor_temperatura import *

def test_celsius_para_fahrenheit_zero():
    assert celsius_para_fahrenheit(0) == 32.00


def test_celsius_para_fahrenheit_valor():
    assert celsius_para_fahrenheit(100) == 212.00


def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0.00

def test_fahrenheit_para_celsius_valor():
    assert fahrenheit_para_celsius(212) == 100.00

def test_entrada_errada_celsius():
    with pytest.raises(TypeError):
        celsius_para_fahrenheit("oi")

def test_entrada_errada_fahrenheit():
    with pytest.raises(TypeError):
        fahrenheit_para_celsius("hi")