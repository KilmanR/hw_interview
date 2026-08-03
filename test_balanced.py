import pytest

from balanced import check_balance, is_balanced


@pytest.mark.parametrize(
    "sequence",
    [
        "(((([{}]))))",
        "[([])((([[[]]])))]{()}",
        "{{[()]}}",
        "()",
        "[]",
        "{}",
        "()[]{}",
        "",
    ],
)
def test_is_balanced_true(sequence):
    assert is_balanced(sequence) is True


@pytest.mark.parametrize(
    "sequence",
    [
        "}{}",
        "{{[(])]}}",
        "[[{())}]",
        "(",
        "[)",
        "([)]",
    ],
)
def test_is_balanced_false(sequence):
    assert is_balanced(sequence) is False


def test_check_balance_returns_messages():
    assert check_balance("(((([{}]))))") == "Сбалансированно"
    assert check_balance("}{}") == "Несбалансированно"
