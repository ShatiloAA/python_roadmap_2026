import pytest

from lesson1.drills import (
    combined,
    evens,
    has_negative,
    indexed,
    letters,
    squares,
    word_lengths,
)


@pytest.mark.parametrize(
    ("nums", "expected"),
    [
        ([1, 2, 3], [1, 4, 9]),
        ([0], [0]),
        ([-1, 100, -100], [1, 10000, 10000]),
    ],
)
def test_squares(nums: list[int], expected: list[int]):
    assert squares(nums) == expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([1, 2, 3], [2]), ([-1, 100, -100], [100, -100]), ([0], [0])],
)
def test_even(nums: list[int], expected: list[int]):
    assert evens(nums) == expected


@pytest.mark.parametrize(
    ("words", "expected"),
    [
        (
            ["a", "b", "c"],
            {
                "a": 1,
                "b": 1,
                "c": 1,
            },
        ),
        ([""], {"": 0}),
        (["less", "fertz", ""], {"less": 4, "fertz": 5, "": 0}),
    ],
)
def test_words_lengths(words: list[str], expected: dict[str, int]):
    assert word_lengths(words) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("bla, bla. bla!", {"a", "l", "b"}),
        ("pressure!", {"p", "s", "u", "r", "e"}),
        ("Aa bB CcC", {"a", "b", "c"}),
    ],
)
def test_letters(text: str, expected: set[str]):
    assert letters(text) == expected


@pytest.mark.parametrize(
    ("nums", "expected"),
    [([-1, 2], True), ([], False), ([0, 1], False), ([0, 1, 2, 3, 4, -5], True)],
)
def test_has_negative(nums: list[int], expected: bool):
    assert has_negative(nums) == expected


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        (["a", "b", "c"], [(0, "a"), (1, "b"), (2, "c")]),
        ([], []),
        ([""], [(0, "")]),
        (["a", "a", "a"], [(0, "a"), (1, "a"), (2, "a")]),
    ],
)
def test_indexed(items: list[str], expected: list[tuple[int, str]]):
    assert indexed(items) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        (["a", "b"], [1, 2], [("a", 1), ("b", 2)]),
        ([], [], []),
        (["", "x"], [0, -1], [("", 0), ("x", -1)]),
    ],
)
def test_combined(a: list[str], b: list[int], expected: list[tuple[str, int]]):
    assert combined(a, b) == expected
