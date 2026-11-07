import pytest

from lesson4.formatters import format_list, format_price


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["яблоко", "грушка", "виноград"], "яблоко, грушка, виноград"),
        (["", "\n", " "], ", \n,  "),
        (["молоко", "", "хлеб", "\n", "язь"], "молоко, , хлеб, \n, язь"),
    ],
)
def test_format_list(items: list[str], expected: str):
    assert format_list(items) == expected


@pytest.mark.parametrize(
    ("price", "expected"),
    [
        (123.321, "123.32 ₽"),
        (100.067, "100.07 ₽"),
        (-1231.64567, "-1231.65 ₽"),
    ],
)
def test_format_price(price: float, expected: str):
    assert format_price(price) == expected
