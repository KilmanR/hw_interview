from stack import Stack

PAIRS = {')': '(', ']': '[', '}': '{'}


def is_balanced(sequence):
    """Проверяет сбалансированность скобочной последовательности."""
    stack = Stack()

    for char in sequence:
        if char in '([{':
            stack.push(char)
        elif char in ')]}':
            if stack.is_empty():
                return False
            if stack.pop() != PAIRS[char]:
                return False

    return stack.is_empty()


def check_balance(sequence):
    """Возвращает сообщение о сбалансированности скобок."""
    if is_balanced(sequence):
        return "Сбалансированно"
    return "Несбалансированно"


if __name__ == "__main__":
    seq = input("Введите строку со скобками: ")
    print(check_balance(seq))
