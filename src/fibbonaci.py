def fibo(n: int) -> int:
    if n < 0:
        raise ValueError("Число Фибоначчи определено только для неотрицательных целых чисел.")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def fibo_recoursive(n: int) -> int:
    if n < 0:
        raise ValueError("Число Фибоначчи определено только для неотрицательных целых чисел.")
    if n <= 1:
        return n        
    return fibo_recoursive(n - 1) + fibo_recoursive(n - 2)