import pytest

from stack import Stack


def test_new_stack_is_empty():
    stack = Stack()
    assert stack.is_empty() is True


def test_push_makes_stack_not_empty():
    stack = Stack()
    stack.push(1)
    assert stack.is_empty() is False


def test_pop_returns_last_pushed():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_peek_does_not_remove():
    stack = Stack()
    stack.push("top")
    assert stack.peek() == "top"
    assert stack.size() == 1


def test_size():
    stack = Stack()
    assert stack.size() == 0
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2


def test_pop_from_empty_raises():
    stack = Stack()
    with pytest.raises(IndexError):
        stack.pop()
