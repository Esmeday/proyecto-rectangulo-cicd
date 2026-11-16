
import pytest

from main import calcular_area


def test_calcular_area():
    assert calcular_area(5, 4) == 21


def test_calcular_area_valores_decimales():
    assert calcular_area(2.5, 4) == 10


def test_base_negativa():
    with pytest.raises(ValueError):
        calcular_area(-5, 4)


def test_altura_cero():
    with pytest.raises(ValueError):
        calcular_area(5, 0)
