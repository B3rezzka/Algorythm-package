import pytest
from src.factorial import factorial, recoursive_factorial


class TestFactorial:
    def test_factorial_zero(self):
        assert factorial(0) == 1

    def test_factorial_one(self):
        assert factorial(1) == 1

    def test_factorial_positive(self):
        assert factorial(5) == 120
        assert factorial(3) == 6

    def test_factorial_negative(self):
        with pytest.raises(ValueError):
            factorial(-1)

    def test_recoursive_factorial_zero(self):
        assert recoursive_factorial(0) == 1

    def test_recoursive_factorial_one(self):
        assert recoursive_factorial(1) == 1

    def test_recoursive_factorial_positive(self):
        assert recoursive_factorial(5) == 120
        assert recoursive_factorial(4) == 24

    def test_recoursive_factorial_negative(self):
        with pytest.raises(ValueError):
            recoursive_factorial(-5)