import pytest
from file import add, subtract, multiply, divide

def test_add():
    assert add(3, 5) == 7

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(2, 3) == 6

def test_divide():
    assert divide(10, 2) == 5