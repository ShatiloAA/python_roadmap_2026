from pathlib import Path

import pytest

from lesson5.json_utils import load_json, save_json, update_json


@pytest.mark.parametrize(
    ("path", "data"),
    [
        (
            "saved_dict.json",
            {
                "obj1": "test1",
                "obj2": "test2",
                "obj3": "test3",
            },
        ),
        ("saved_list.json", ["a", "b", "c"]),
        ("empty_dict.json", {}),
        ("empty_list.json", []),
        (
            "nested_dict.json",
            {
                "obj1": {"field1": "value1", "field2": "value2"},
                "obj2": [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
            },
        ),
    ],
)
def test_save_and_load_json(tmp_path: Path, path: Path, data: dict | list) -> None:
    file = tmp_path / path
    save_json(file, data)
    result = load_json(file)
    assert data == result


@pytest.mark.parametrize(
    ("path", "test_data", "key", "value", "expected"),
    [
        (
            "saved_dict.json",
            {
                "obj1": "test1",
                "obj2": "test2",
                "obj3": "test3",
            },
            "obj2",
            "modified_test2",
            {
                "obj1": "test1",
                "obj2": "modified_test2",
                "obj3": "test3",
            },
        ),
        (
            "empty_dict.json",
            {},
            "added_key",
            "added_value",
            {"added_key": "added_value"},
        ),
        (
            "nested_dict.json",
            {
                "obj1": {"field1": "value1", "field2": "value2"},
                "obj2": [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
            },
            "obj1",
            ["new_value"],
            {
                "obj1": ["new_value"],
                "obj2": [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
            },
        ),
    ],
)
def test_update_json(
    tmp_path: Path, path: Path, test_data: dict, key: str, value, expected: dict
) -> None:
    file = tmp_path / path
    if test_data:
        save_json(file, test_data)

    result = update_json(file, key, value)

    assert result == expected


@pytest.mark.parametrize(
    ("path", "test_data"),
    [
        ("saved_list.json", ["a", "b", "c"]),
        ("saved_tuple.json", ("a", "b", "c")),
    ],
)
def test_update_json_not_ok(tmp_path: Path, path: Path, test_data):
    file = tmp_path / path
    save_json(file, test_data)
    with pytest.raises(TypeError):
        _ = update_json(file, "", "")
