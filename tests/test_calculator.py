from src.calculator import add, multiply, average

def test_add():
    assert add(2, 3) == 5

def test_multiply():
    assert multiply(4, 5) == 20

def test_average():
    assert average([2, 4, 6]) == 4