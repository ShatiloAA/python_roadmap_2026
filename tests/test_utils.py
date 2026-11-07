import pytest

from lesson4.utils import cube, is_even, square


@pytest.mark.parametrize(
    ("x", "expected"), [(2, 8), (0, 0), (-1, -1), (1.2, 1.7279999999999998)]
)
def test_cube(x: float, expected: float) -> None:
    assert cube(x) == expected


@pytest.mark.parametrize(("x", "expected"), [(2, 4), (0, 0), (-1, 1), (1.2, 1.44)])
def test_square(x: float, expected: float) -> None:
    assert square(x) == expected


@pytest.mark.parametrize(
    ("x", "expected"), [(2, True), (0, True), (-1, False), (-4.0, True)]
)
def test_is_even(x: int, expected: bool) -> None:
    assert is_even(x) == expected
