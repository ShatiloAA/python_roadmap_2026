from pathlib import Path

import pytest

from lesson3.files import append_line, count_words, read_all, write_lines

TEST_DIR = Path(__file__).parent


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("empty.txt", ""),
        (Path("empty.txt"), ""),
        (Path("only_newlines.txt"), "\n\n\n\n\n\n\n\n\n\n\n\n\n\n"),
        (
            Path("some_text.txt"),
            "\nПочему это супер-полезная фишка?\n\nИменно благодаря этому свойству можно писать «безопасные» функции. Представьте, что вы пишете функцию чтения логов, и хотите, чтобы пользователь мог передать туда и строку, и готовый Path\n",
        ),
    ],
)
def test_read_all_ok(path: str | Path, expected: str) -> None:
    assert read_all(TEST_DIR / "data" / path) == expected


@pytest.mark.parametrize(
    ("path"),
    [
        # "",
        # Path(""),
        Path("not_found.txt"),
    ],
)
def test_read_all_with_exception(path: str | Path) -> None:
    with pytest.raises(FileNotFoundError):
        read_all(TEST_DIR / "data" / path)


@pytest.mark.parametrize(
    ("path", "lines", "expected"),
    [
        ("write_lines", ["a", "b", "c"], "a\nb\nc\n"),
        (
            "only_newlines.txt",
            [
                "\n",
                "\n",
                "\n",
                "\n",
                "\n",
                "\n",
                "\n",
            ],
            "\n\n\n\n\n\n\n\n\n\n\n\n\n\n",
        ),
        (
            "only_whitespaces.txt",
            [
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
                " ",
            ],
            " \n \n \n \n \n \n \n",
        ),
    ],
)
def test_write_lines_ok(path: str | Path, lines: list[str], expected: str):
    full_path = TEST_DIR / "data" / path
    write_lines(path=full_path, lines=lines)
    assert read_all(full_path) == expected


@pytest.mark.parametrize(
    ("path", "lines"),
    [
        ("fake_name_write_lines", ["a", "b", "c"]),
    ],
)
def test_write_lines_with_exception(path: str | Path, lines: list[str]):
    full_path = TEST_DIR / "data" / "fake" / path
    with pytest.raises(FileNotFoundError):
        write_lines(path=full_path, lines=lines)


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        ("some_text.txt", 31),
        ("only_whitespaces.txt", 0),
        ("only_newlines.txt", 0),
        ("empty.txt", 0),
    ],
)
def test_count_words_ok(path: str | Path, expected: int):
    assert count_words(TEST_DIR / "data" / path) == expected


@pytest.mark.parametrize(
    ("path"),
    [
        ("fake_file_count_words.txt"),
    ],
)
def test_count_words_with_exception(path: str | Path):
    full_path = TEST_DIR / "data" / path
    with pytest.raises(FileNotFoundError):
        count_words(path=full_path)


@pytest.mark.parametrize(
    ("path", "start", "line", "expected"),
    [
        ("new_file_to_append.txt", [], "test_line", "test_line\n"),
        ("append_line.txt", ["first line"], "second line", "first line\nsecond line\n"),
    ],
)
def test_append_line_ok(path: str | Path, start: list[str], line: str, expected: str):
    full_path = TEST_DIR / "data" / path
    write_lines(full_path, start)
    append_line(full_path, line)
    assert read_all(full_path) == expected


@pytest.mark.parametrize(
    ("path"),
    [
        ("fake_name_write_lines"),
    ],
)
def test_append_line_with_exception(path: str | Path):
    full_path = TEST_DIR / "data" / "fake" / path
    with pytest.raises(FileNotFoundError):
        append_line(full_path, "line")
