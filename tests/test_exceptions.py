import pytest

from lesson2.exceptions import (
    NotPositiveError,
    parse_int,
    safe_divide,
    validate_age,
    validate_positive,
)


@pytest.mark.parametrize(
    ("a", "b", "expected"), [(1, 2, 0.5), (2, 0.5, 4.0), (0.1, 0.1, 1.0)]
)
def test_safe_divide_ok(a: float, b: float, expected: float):
    assert safe_divide(a, b) == expected


@pytest.mark.parametrize(("a", "b"), [(2, 0), (0, 0), (-1, -0), (12, +0)])
def test_safe_divide_with_exception(a: float, b: float):
    with pytest.raises(ZeroDivisionError):
        safe_divide(a, b)


@pytest.mark.parametrize(("s", "expected"), [("+1", 1), ("-2", -2), ("000", 0)])
def test_parse_int_ok(s: str, expected: int):
    assert parse_int(s) == expected


@pytest.mark.parametrize(("s"), [("a"), ("1.2")])
def test_parse_int_with_exception(s: str):
    with pytest.raises(ValueError):
        parse_int(s)


@pytest.mark.parametrize(("age", "expected"), [(0, 0), (-0, 0), (150, 150), (100, 100)])
def test_validate_age_ok(age: int, expected: int):
    assert validate_age(age) == expected


@pytest.mark.parametrize(("age"), [(-1), (151)])
def test_validate_age_with_exception(age: int):
    with pytest.raises(ValueError):
        validate_age(age)


@pytest.mark.parametrize(("name", "value", "expected"), [("c", 1, 1)])
def test_validate_positive(name: str, value: int, expected: int):
    assert validate_positive(name, value) == expected


@pytest.mark.parametrize(("name", "value"), [("a", -0), ("b", -1), ("d", 0)])
def test_validate_positive_with_exception(name: str, value: int):
    with pytest.raises(NotPositiveError):
        validate_positive(name, value)
