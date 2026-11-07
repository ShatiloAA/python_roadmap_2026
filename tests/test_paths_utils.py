from pathlib import Path

import pytest

from lesson5.paths_utils import ensure_dir, get_data_dir, list_files

TEST_DIR = Path(__file__).parent
NEW_DIR = Path(TEST_DIR) / "data" / "test"


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        (Path("test"), Path("test/data")),
        ("", Path("data")),
        (".", Path("./data")),
    ],
)
def test_get_data_dir(path: str | Path, expected: Path) -> None:
    assert get_data_dir(path) == expected


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        (Path(TEST_DIR), Path(TEST_DIR)),
        (Path(NEW_DIR), Path(NEW_DIR)),
    ],
)
def test_ensure_dir(path: str | Path, expected: Path):
    folder = Path(NEW_DIR)
    if folder.is_dir():
        folder.rmdir()
    assert ensure_dir(path) == expected


@pytest.mark.parametrize(
    ("ext", "files", "expected"),
    [
        (
            ".txt",
            [
                Path("append_line.txt"),
                Path("empty"),
                Path("new_file_to_append.txt"),
                Path("only_newlines.txt"),
                Path("only_whitespaces.txt"),
                Path("write_lines.txt"),
            ],
            [
                Path("append_line.txt"),
                Path("new_file_to_append.txt"),
                Path("only_newlines.txt"),
                Path("only_whitespaces.txt"),
                Path("write_lines.txt"),
            ],
        ),
        (
            "txt",
            [
                Path("append_line.txt"),
                Path("empty"),
                Path("new_file_to_append.txt"),
                Path("only_newlines.txt"),
                Path("only_whitespaces.txt"),
                Path("write_lines.txt"),
            ],
            [
                Path("append_line.txt"),
                Path("new_file_to_append.txt"),
                Path("only_newlines.txt"),
                Path("only_whitespaces.txt"),
                Path("write_lines.txt"),
            ],
        ),
        (
            None,
            [
                Path("append_line.txt"),
                Path("empty"),
                Path("new_file_to_append.txt"),
                Path("only_newlines.txt"),
                Path("only_whitespaces.txt"),
                Path("write_lines.txt"),
            ],
            [
                "append_line.txt",
                "empty",
                "new_file_to_append.txt",
                "only_newlines.txt",
                "only_whitespaces.txt",
                "write_lines.txt",
            ],
        ),
        (
            "",
            [
                Path("append_line.txt"),
                Path("empty"),
                Path("new_file_to_append.txt"),
                Path("only_newlines.txt"),
                Path("only_whitespaces.txt"),
                Path("write_lines.txt"),
            ],
            [Path("empty")],
        ),
        (
            "py",
            [
                Path("test_drills.py"),
                Path("test_exceptions.py"),
                Path("test_files.py"),
                Path("test_formatters.py"),
                Path("test_idioms.py"),
                Path("test_main.py"),
                Path("test_paths_utils.py"),
                Path("test_utils.py"),
                Path("append_line.txt"),
                Path("empty"),
                Path("new_file_to_append.txt"),
                Path("only_newlines.txt"),
                Path("only_whitespaces.txt"),
                Path("write_lines.txt"),
            ],
            [
                Path("test_drills.py"),
                Path("test_exceptions.py"),
                Path("test_files.py"),
                Path("test_formatters.py"),
                Path("test_idioms.py"),
                Path("test_main.py"),
                Path("test_paths_utils.py"),
                Path("test_utils.py"),
            ],
        ),
        (
            ".py",
            [
                Path("test_drills.py"),
                Path("test_exceptions.py"),
                Path("test_files.py"),
                Path("test_formatters.py"),
                Path("test_idioms.py"),
                Path("test_main.py"),
                Path("test_paths_utils.py"),
                Path("test_utils.py"),
                Path("append_line.txt"),
                Path("empty"),
                Path("new_file_to_append.txt"),
                Path("only_newlines.txt"),
                Path("only_whitespaces.txt"),
                Path("write_lines.txt"),
            ],
            [
                Path("test_drills.py"),
                Path("test_exceptions.py"),
                Path("test_files.py"),
                Path("test_formatters.py"),
                Path("test_idioms.py"),
                Path("test_main.py"),
                Path("test_paths_utils.py"),
                Path("test_utils.py"),
            ],
        ),
        # (None, [], []),
    ],
)
def test_list_files(
    tmp_path: Path, ext: str | None, files: list[Path], expected: list[Path]
):
    added_dir = tmp_path / "added_dir"
    added_dir.mkdir()
    [(tmp_path / f).touch() for f in files]
    print(tmp_path.iterdir())

    assert list_files(tmp_path, ext) == [tmp_path / e for e in expected]
