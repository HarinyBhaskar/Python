# test_cart.py
import pytest
from cart import Cart

def test_total():
    c = Cart()
    c.add_item("apple", 10)
    c.add_item("banana", 20)
    assert c.total() == 30

def test_invalid_price():
    c = Cart()
    with pytest.raises(ValueError):
        c.add_item("mango", -5)
