# test_calculator.py
import pytest
from calculator import Calculator

@pytest.fixture
def calc():
    return Calculator()

def test_add(calc):
    assert calc.add(1, 2) == 3
    assert calc.add(-1, 1) == 0
    assert calc.add(-1, -1) == -2

def test_subtract(calc):
    assert calc.subtract(10, 5) == 5
    assert calc.subtract(-1, -1) == 0
    assert calc.subtract(-1, 1) == -2

def test_multiply(calc):
    assert calc.multiply(3, 7) == 21
    assert calc.multiply(-1, 1) == -1
    assert calc.multiply(-1, -1) == 1

def test_divide(calc):
    assert calc.divide(10, 2) == 5
    assert calc.divide(-10, 2) == -5
    assert calc.divide(-10, -2) == 5
    with pytest.raises(ValueError):
        calc.divide(10, 0)


