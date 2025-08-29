from decorator_demo import multiply

def test_multiply_positive():
    assert multiply(3, 4) == 12

def test_multiply_with_zero():
    assert multiply(5, 0) == 0

def test_multiply_negative():
    assert multiply(-2, 3) == -6
