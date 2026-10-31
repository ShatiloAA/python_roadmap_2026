from pathlib import Path

# def show_logs(file_name: Path) -> None:
#     try:
#         with open(file_name, "r", encoding='urf-8'):
#             print(s) for s in Path.read_text()
#     except FileNotFoundError:
#         print("Файл еще не создан. Запустите запись.")


def read_all(path: str | Path) -> str:
    with open(Path(path), "r", encoding="utf-8") as f:
        return f.read()


def write_lines(path: str | Path, lines: list[str]) -> None:
    with open(Path(path), "w", encoding="utf-8") as f:
        f.writelines(f"{line}\n" for line in lines)


def count_words(path: str | Path) -> int:
    s = Path(path).read_text(encoding="utf-8")
    words = s.split()
    return len(words)


def append_line(path: str | Path, line: str) -> None:
    with open(Path(path), "a", encoding="utf-8") as f:
        f.writelines(f"{line}\n")
