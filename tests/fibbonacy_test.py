import pytest
from src.fibbonaci import fibo, fibo_recoursive


class TestFibo:
    def test_fibo_zero(self):
        assert fibo(0) == 0

    def test_fibo_one(self):
        assert fibo(1) == 1

    def test_fibo_positive(self):
        assert fibo(10) == 55
        assert fibo(5) == 5

    def test_fibo_negative(self):
        with pytest.raises(ValueError):
            fibo(-1)

    def test_fibo_recursive_zero(self):
        assert fibo_recoursive(0) == 0

    def test_fibo_recursive_one(self):
        assert fibo_recoursive(1) == 1

    def test_fibo_recursive_positive(self):
        assert fibo_recoursive(10) == 55
        assert fibo_recoursive(6) == 8

    def test_fibo_recursive_negative(self):
        with pytest.raises(ValueError):
            fibo_recoursive(-10)