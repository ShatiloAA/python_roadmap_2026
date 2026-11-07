from pathlib import Path


def get_data_dir(base: str | Path) -> Path:
    return Path(base) / "data"


def ensure_dir(path: str | Path) -> Path:
    directory = Path(path)
    directory.mkdir(parents=True, exist_ok=True)

    return directory


def list_files(path: str | Path, ext: str | None = None) -> list[Path]:
    directory = Path(path)

    if ext is None:
        suffix = None
    elif ext == "":
        suffix = ""
    else:
        suffix = f".{ext}" if not ext.startswith(".") else ext

    files = [item for item in directory.iterdir() if item.is_file()]
    if suffix is not None:
        files = [item for item in files if item.suffix == suffix]

    return sorted(files, key=lambda p: p.name)
