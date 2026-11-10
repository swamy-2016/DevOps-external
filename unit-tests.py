def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def test_divide():
    assert divide(6, 2) == 3
    assert divide(6, -2) == -3
    assert divide(-6, -2) == 3
    try:
        divide(6, 0)
        assert False, "Expected ValueError"
    except ValueError:
        pass

def MaxOfThree(a, b, c):
    if(a >= b and a >= c):
        return a
    if(b >= a and b >= c):
        return b
    return c

def test_MaxOfThree():
    assert MaxOfThree(1, 2, 3) == 3
    assert MaxOfThree(3, 2, 1) == 3
    assert MaxOfThree(1, 3, 2) == 3


def Compare(a, b):
    return a>b

def test_Compare():
    assert Compare(3, 2) == True
    assert Compare(2, 3) == False
    assert Compare(3, 3) == False

