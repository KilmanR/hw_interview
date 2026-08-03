class Stack:
    """Стек — элементы, организованные по принципу LIFO.

    Последним пришёл — первым вышел.
    """

    def __init__(self):
        self._items = []

    def is_empty(self):
        """Проверяет стек на пустоту."""
        return len(self._items) == 0

    def push(self, item):
        """Добавляет новый элемент на вершину стека."""
        self._items.append(item)

    def pop(self):
        """Удаляет верхний элемент стека и возвращает его."""
        return self._items.pop()

    def peek(self):
        """Возвращает верхний элемент стека, не удаляя его."""
        return self._items[-1]

    def size(self):
        """Возвращает количество элементов в стеке."""
        return len(self._items)
