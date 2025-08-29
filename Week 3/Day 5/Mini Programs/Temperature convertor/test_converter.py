# test_converter.py
from converter import c_to_f, f_to_c

def test_c2f():
    assert c_to_f(0) == 32

def test_f2c():
    assert round(f_to_c(32), 2) == 0
