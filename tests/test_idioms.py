import pytest

from lesson1.idioms import index_words, is_palindrome, top_words, unique_words


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", True),
        ("A", True),
        ("apa", True),
        ("А роза, упала на лапу Азора!", True),
        ("abc: cba", True),
    ],
)
def test_is_palindrome(text: str, expected: bool) -> None:
    assert is_palindrome(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", []),
        ("a a b", [("a", 2), ("b", 1)]),
        ("A a b", [("a", 2), ("b", 1)]),
        ("the cat sat on the mat", [("the", 2), ("cat", 1), ("mat", 1)]),
    ],
)
def test_top_words(text: str, expected: list) -> None:
    assert top_words(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("Hi hi", [(0, "hi"), (1, "hi")]),
        ("", []),
        ("a b c d", [(0, "a"), (1, "b"), (2, "c"), (3, "d")]),
    ],
)
def test_index_words(text: str, expected: list) -> None:
    assert index_words(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("a b c d a c b e f", ["a", "b", "c", "d", "e", "f"]),
        ("", []),
        ("Fu fu Fu fu", ["fu"]),
    ],
)
def test_unique_words(text: str, expected: list) -> None:
    assert unique_words(text) == expected
