from src.main import (add,subtract)
def test_add_function():
    assert add(3,4) == 7
    assert add(6,8) == 14
    
def test_subtract_function():
    assert subtract(6,4)==2
    assert subtract(4,2) == 2

