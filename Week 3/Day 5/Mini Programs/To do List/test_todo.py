# test_todo.py
import pytest
from todo import Todo

def test_add_remove():
    t = Todo()
    t.add_task("Learn Python")
    assert t.remove_task("Learn Python")

def test_empty_add():
    t = Todo()
    with pytest.raises(ValueError):
        t.add_task("   ")
