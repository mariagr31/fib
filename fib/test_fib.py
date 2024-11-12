from fib.fibonacci import fibonacci_recursive
from fibonacci import fibonacci_iterative
import pytest

def test_fib_9_is_34():
    assert fibonacci_iterative(9) == 34

def test_fib_negative_raise_error():
    pass

def test_fib_negative_raise_error():
    with pytest.raises(ValueError):
        fibonacci_iterative(-1)

def test_fib_cache():
    assert fibonacci_recursive(9)