
def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative number is unexpected")
    result = 1
    for _ in range(1, (n + 1)):
        result *= _
    return result

def recoursive_factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negative number is unexpected")
    elif n <=1:
        return 1
    else:
        return n * recoursive_factorial(n - 1)