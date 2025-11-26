def bubble_sort(arr : list[int]) -> list[int]:
    """
    Пузырьковая сортировка.
    """
    if len(arr) <= 1:
        return arr
    l = len(arr)
    lst = arr.copy()
    for i in range(l):
        swapped = False
        for j in range(0, l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def quick_sort(arr: list[int]) -> list[int]:
    """
    Быстрая сортировка.
    """
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def counting_sort(arr: list[int]) -> list[int]:
    """
    Сортировка с подсчётом.
    """
    if len(arr) <= 1:
        return arr
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i + min_val] * cnt)

    return sorted_arr

def radix_sort(arr: list[int], base: int = 10) -> list[int]:
    """
    Поразрядная сортировка.
    """
    if len(arr) <= 1:
        return arr
    # Обработка отрицательных чисел: разделим на положительные и отрицательные
    positive = [x for x in arr if x >= 0]
    negative = [-x for x in arr if x < 0]
    negative.reverse() # Разворачиваем для правильного порядка при сортировке
    if positive:
        max_num = max(positive)
        exp = 1
        while max_num // exp > 0:
            positive = counting_sort_for_radix(positive, exp, base)
            exp *= base
    if negative:
        max_neg = max(negative)
        exp = 1
        while max_neg // exp > 0:
            negative = counting_sort_for_radix(negative, exp, base)
            exp *= base
        negative.reverse() # Разворачиваем обратно
        negative = [-x for x in negative]
    return negative + positive

def counting_sort_for_radix(arr, exp, base):
    """
    Вспомогательная функция для radix_sort.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * base
    for i in range(n):
        index = (arr[i] // exp) % base
        count[index] += 1
    for i in range(1, base):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1
    return output

def bucket_sort(arr: list[float], buckets: int | None = None) -> list[float]:
    """
    Сортировка корзинами (для чисел в [0, 1)).
    """
    if len(arr) <= 1:
        return arr
    if buckets is None:
        buckets = len(arr)
    # Нормализация для чисел в [0, 1)
    # Предполагается, что все числа входят в диапазон [0, 1)
    bucket_list = [[] for _ in range(buckets)]
    for num in arr:
        # Индекс корзины: num * buckets, ограниченный [0, buckets - 1]
        index = min(int(num * buckets), buckets - 1)
        bucket_list[index].append(num)
    sorted_arr = []
    for bucket in bucket_list:
        sorted_arr.extend(quick_sort(bucket))
    return sorted_arr

def heap_sort(arr: list[int]) -> list[int]:
    """Сортировка кучей."""
    lst = arr.copy()
    n = len(arr)
    # Построение max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    # Извлечение элементов из кучи
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)
    return arr

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)