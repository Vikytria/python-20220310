from calculator import add

def test_add():
    # when
    result = add(5, 10)
    # Then
    assert result == 15

def test_add_with_negative_numbers():
    result = add(-1, -2)
    assert result == -3

def test_add_with_float():
    result = add(3.4, 6.3)
    assert result == 9.7