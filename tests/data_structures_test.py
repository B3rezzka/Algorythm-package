import pytest
from src.data_structure import Stack, Queue


class TestStack:
    def test_push_pop_peek(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(3)
        assert s.peek() == 3
        assert s.pop() == 3
        assert s.pop() == 2
        assert s.peek() == 1
        assert len(s) == 1

    def test_is_empty(self):
        s = Stack()
        assert s.is_empty() is True
        s.push(1)
        assert s.is_empty() is False
        s.pop()
        assert s.is_empty() is True

    def test_pop_empty(self):
        s = Stack()
        with pytest.raises(IndexError, match="pop from empty stack"):
            s.pop()

    def test_peek_empty(self):
        s = Stack()
        with pytest.raises(IndexError, match="peek from empty stack"):
            s.peek()

    def test_min_basic(self):
        s = Stack()
        s.push(3)
        assert s.min() == 3
        s.push(5)
        assert s.min() == 3
        s.push(2)
        assert s.min() == 2
        s.push(7)
        assert s.min() == 2
        s.pop() # pop 7
        assert s.min() == 2
        s.pop() # pop 2
        assert s.min() == 3
        s.pop() # pop 5
        assert s.min() == 3
        s.pop() # pop 3
        assert len(s) == 0

    def test_min_empty(self):
        s = Stack()
        with pytest.raises(ValueError, match="min from empty stack"):
            s.min()

    def test_min_with_duplicates(self):
        s = Stack()
        s.push(1)
        s.push(2)
        s.push(1)
        assert s.min() == 1
        s.pop() # pop 1
        assert s.min() == 1
        s.pop() # pop 2
        assert s.min() == 1

class TestQueue:
    def test_enqueue_dequeue_front(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        assert q.front() == 1
        assert q.dequeue() == 1
        assert q.dequeue() == 2
        assert q.front() == 3
        assert len(q) == 1

    def test_is_empty(self):
        q = Queue()
        assert q.is_empty() is True
        q.enqueue(1)
        assert q.is_empty() is False
        q.dequeue()
        assert q.is_empty() is True

    def test_dequeue_empty(self):
        q = Queue()
        with pytest.raises(IndexError, match="dequeue from empty queue"):
            q.dequeue()

    def test_front_empty(self):
        q = Queue()
        with pytest.raises(IndexError, match="front from empty queue"):
            q.front()