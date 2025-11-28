from src.factorial import factorial, recoursive_factorial
from src.fibbonaci import fibo, fibo_recoursive
from src.sortings import bubble_sort, quick_sort, counting_sort, radix_sort, bucket_sort, heap_sort
from src.data_structure import Stack
from src.utils import rand_int_array, nearly_sorted, many_duplicates, reverse_sorted, rand_float_array

if __name__ == "__main__":
    print("=== Факториал и Фибоначчи ===")
    print(f"5! = {factorial(5)}")
    print(f"5! (рекурсивно) = {recoursive_factorial(5)}")
    print(f"F(10) = {fibo(10)}")
    print(f"F(10) (рекурсивно) = {fibo_recoursive(10)}\n")

    print("=== Сортировки ===")
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Исходный массив: {arr}")
    print(f"Bubble Sort: {bubble_sort(arr)}")
    print(f"Quick Sort: {quick_sort(arr)}")
    print(f"Counting Sort: {counting_sort(arr)}")
    print(f"Radix Sort: {radix_sort(arr)}")
    print(f"Heap Sort: {heap_sort(arr)}")
    # Bucket Sort для [0,1)
    float_arr = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
    print(f"Bucket Sort: {bucket_sort(float_arr)}\n")

    print("=== Стек с минимумом ==")
    stack = Stack()
    values = [3, 5, 2, 1, 4]
    for v in values:
        stack.push(v)
        print(f"Push {v}, min = {stack.min()}")
    while not stack.is_empty():
        print(f"Pop {stack.pop()}, min = {stack.min() if not stack.is_empty() else 'N/A'}\n")

    print("=== Генерация тест-кейсов ===")
    print(f"Случайный массив [0, 100]: {rand_int_array(10, 0, 100, seed=4)}")
    print(f"Почти отсортированный: {nearly_sorted(10, 3, seed=52)}")
    print(f"С дубликатами: {many_duplicates(10, k_unique=3, seed=42)}")
    print(f"Обратно отсортированный: {reverse_sorted(10)}")
    print(f"Случайный float [0, 1): {rand_float_array(5, seed=1487)}")
