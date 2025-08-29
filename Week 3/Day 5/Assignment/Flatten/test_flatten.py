from flatten import flatten

def test_simple_list():
    assert flatten([1, [2, 3]]) == [1, 2, 3]

def test_nested_list():
    assert flatten([1, [2, [3, 4]], 5]) == [1, 2, 3, 4, 5]

def test_empty_list():
    assert flatten([]) == []
