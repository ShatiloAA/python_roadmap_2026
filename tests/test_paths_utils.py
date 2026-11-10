from pathlib import Path

import pytest

from lesson5.paths_utils import ensure_dir, get_data_dir, list_files


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
        (Path("new_dir"), Path("new_dir")),
    ],
)
def test_ensure_dir_new_dir(tmp_path: Path, path: str | Path, expected: Path):
    folder = tmp_path / path
    assert not folder.is_dir()
    assert ensure_dir(folder) == tmp_path / expected
    assert folder.is_dir()


@pytest.mark.parametrize(
    ("path", "expected"),
    [
        (Path("exist_dir"), Path("exist_dir")),
    ],
)
def test_ensure_dir_exist_dir(tmp_path: Path, path: str | Path, expected: Path):
    folder = tmp_path / path
    folder.mkdir()
    assert ensure_dir(folder) == tmp_path / expected
    assert folder.is_dir()


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
        (None, [], []),
    ],
)
def test_list_files(
    tmp_path: Path, ext: str | None, files: list[Path], expected: list[Path]
):
    added_dir = tmp_path / "added_dir"
    added_dir.mkdir()
    for f in files:
        (tmp_path / f).touch()

    assert list_files(tmp_path, ext) == [tmp_path / e for e in expected]
