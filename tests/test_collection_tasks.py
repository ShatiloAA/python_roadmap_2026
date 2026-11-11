import pytest

from lesson6.collection_tasks import (
    common_elements,
    count_chars,
    group_by_length,
    unique_in_order,
)


@pytest.mark.parametrize(
    ("items", "expected"),
    [
        ([], []),
        ([""], [""]),
        (["a"], ["a"]),
        (["a", "a"], ["a"]),
        (["a", "A"], ["a", "A"]),
        (["a", "b", "a", "c", "a", "b"], ["a", "b", "c"]),
    ],
)
def test_unique_in_order(items: list[str], expected: list[str]):
    assert unique_in_order(items) == expected


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        ([], [], set()),
        ([1], [2], set()),
        ([1], [-1], set()),
        ([1, 2, 3], [2, 3, 4], {2, 3}),
        ([3, 3, 3], [3, 3, 0], {3}),
    ],
)
def test_common_elements(a: list[int], b: list[int], expected: set[int]):
    assert common_elements(a, b) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("", {}),
        ("\n", {"\n": 1}),
        ("alaverdy", {"a": 2, "l": 1, "v": 1, "e": 1, "r": 1, "d": 1, "y": 1}),
        ("абракадабара", {"а": 6, "б": 2, "р": 2, "к": 1, "д": 1}),
        ("аааааа ", {"а": 6, " ": 1}),
        ("а аа аа а ", {"а": 6, " ": 4}),
    ],
)
def test_count_chars(text: str, expected: dict[str, int]):
    assert count_chars(text) == expected


@pytest.mark.parametrize(
    ("words", "expected"),
    [
        ([], {}),
        ([""], {0: [""]}),
        (["", ""], {0: ["", ""]}),
        (["\n"], {1: ["\n"]}),
        (
            ["a", "b", "aa", "c", "bbb", "cc"],
            {1: ["a", "b", "c"], 2: ["aa", "cc"], 3: ["bbb"]},
        ),
        (
            ["a", "aa", "aaa", "a", "aaa", "aa"],
            {
                1: ["a", "a"],
                2: ["aa", "aa"],
                3: ["aaa", "aaa"],
            },
        ),
    ],
)
def test_group_by_length(words: list[str], expected: dict[int, list[str]]):
    assert group_by_length(words) == expected
