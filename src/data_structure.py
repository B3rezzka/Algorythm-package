class Stack:
    """
    Стек, реализованный на основе встроенной list.
    Поддерживает операции push, pop, peek, is_empty, len.
    """

    def __init__(self):
        self._items = []
        """
        Вспомогательный стек для хранения минимальных значений
        На вершине всегда находится минимальный элемент основного стека
        """
        self._min_stack = []

    def push(self, x: int) -> None:
        """
        Добавляет элемент x на вершину стека.
        """
        self._items.append(x)
        """
        Обновляем _min_stack
        Если _min_stack пуст или x меньше или равен текущему минимуму,
        добавляем x в _min_stack
        """
        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)

    def pop(self) -> int:
        """Удаляет и возвращает элемент с вершины стека."""
        if self.is_empty():
            raise IndexError("pop from empty stack")

        val = self._items.pop()
        """
        Если удаленный элемент был минимальным,
        удаляем его и из _min_stack
        """
        if self._min_stack and val == self._min_stack[-1]:
            self._min_stack.pop()

        return val

    def peek(self) -> int:
        """
        Возвращает элемент с вершины стека без удаления.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def min(self) -> int:
        """
        Возвращает минимальный элемент в стеке за O(1).
        Требует модификации push/pop для корректной работы.
        """
        if not self._min_stack:
            raise ValueError("min from empty stack")
        return self._min_stack[-1]

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.
        """
        return len(self._items) == 0

    def __len__(self) -> int:
        """
        Возвращает количество элементов в стеке.
        """
        return len(self._items)


class Queue:
    """
    Очередь, реализованная на основе встроенной list.
    Поддерживает операции enqueue, dequeue, front, is_empty, len.
    """

    def __init__(self):
        self._items = []

    def enqueue(self, x: int) -> None:
        """Добавляет элемент x в начало очереди."""
        self._items.insert(0, x)

    def dequeue(self) -> int:
        """
        Удаляет и возвращает элемент из начала очереди.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        """
        Поп из начала списка O(n), но для простоты и соответствия требованиям
        используем встроенный list. Для O(1) dequeue можно использовать collections.deque.        
        """
        return self._items.pop(0)

    def front(self) -> int:
        """
        Возвращает элемент из начала очереди без удаления.
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли очередь.
        """
        return len(self._items) == 0

    def __len__(self) -> int:
        """
        Возвращает количество элементов в очереди.
        """
        return len(self._items)
