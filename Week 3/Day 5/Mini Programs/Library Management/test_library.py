# test_library.py
import pytest
from library import Library

def test_add_and_search():
    lib = Library()
    lib.add_book("Python 101")
    assert lib.has_book("Python 101")

def test_empty_title():
    lib = Library()
    with pytest.raises(ValueError):
        lib.add_book("   ")
