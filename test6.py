'''
Prepare a test for factorial function.
'''
import pytest

def factorial(n:int) -> int:
    if n < 0:
        raise NegativeValueError("Negative values are not allowed")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

class NegativeValueError(Exception):
    pass

class Test_factorial:
    def test_factorial(self):
        # given
        n = 5
        # when
        result = factorial(n)
        # then
        assert result == 120, f"Expected 120 but got {result}"
    
    def test_factorial_zero(self):
        # given
        n = 0
        # when
        result = factorial(n)
        # then
        assert result == 1, f"Expected 1 but got {result}"
    def test_factorial_negative(self):
        # given
        n = -5
        # when
        with pytest.raises(NegativeValueError):
            factorial(n)
