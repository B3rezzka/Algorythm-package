import random

def rand_int_array(n: int, lo: int, hi: int, *, distinct=False, seed=None) -> list[int]:
    """
    Генерирует массив случайных целых чисел.
    Args:
        n: Количество элементов.
        lo: Минимальное значение (включительно).
        hi: Максимальное значение (включительно).
        distinct: Если True, все элементы будут уникальными.
        seed: Зерно для генератора случайных чисел.
    """
    if seed is not None:
        random.seed(seed)
    if distinct:
        if hi - lo + 1 < n:
             raise ValueError("Недостаточно уникальных значений для заданных lo, hi, n")
        return random.sample(range(lo, hi + 1), n)
    else:
        return [random.randint(lo, hi) for _ in range(n)]

def nearly_sorted(n: int, swaps: int, *, seed=None) -> list[int]:
    """
    Генерирует почти отсортированный массив.
    Args:
        n: Количество элементов.
        swaps: Количество случайных перестановок в отсортированном массиве.
        seed: Зерно для генератора случайных чисел.
    """
    if seed is not None:
        random.seed(seed)
    arr = list(range(n))
    for _ in range(swaps):
        i, j = random.randint(0, n-1), random.randint(0, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    return arr

def many_duplicates(n: int, k_unique=5, *, seed=None) -> list[int]:
    """
    Генерирует массив с большим количеством дубликатов.

    Args:
        n: Количество элементов.
        k_unique: Количество уникальных значений.
        seed: Зерно для генератора случайных чисел.

    Returns:
        Список с повторяющимися элементами.
    """
    if seed is not None:
        random.seed(seed)
    unique_vals = rand_int_array(k_unique, 0, k_unique * 10, distinct=True, seed=seed)
    return [random.choice(unique_vals) for _ in range(n)]

def reverse_sorted(n: int) -> list[int]:
    """
    Генерирует отсортированный в обратном порядке массив.
    Args:
        n: Количество элементов.
    """
    return list(range(n-1, -1, -1))

def rand_float_array(n: int, lo=0.0, hi=1.0, *, seed=None) -> list[float]:
    """
    Генерирует массив случайных вещественных чисел.
    Args:
        n: Количество элементов.
        lo: Минимальное значение (включительно).
        hi: Максимальное значение (включительно).
        seed: Зерно для генератора случайных чисел.
    """
    if seed is not None:
        random.seed(seed)
    return [random.uniform(lo, hi) for _ in range(n)]
