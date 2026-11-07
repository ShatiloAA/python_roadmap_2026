import json
from pathlib import Path


def save_json(path: str | Path, data: dict | list) -> None:
    with open(Path(path), "w", encoding="utf-8") as f:
        json.dump(obj=data, ensure_ascii=False, indent=2, fp=f)


def load_json(path: str | Path) -> dict | list:
    with open(Path(path), "r", encoding="utf-8") as f:
        return json.load(f)


def update_json(path: str | Path, key: str, value: object) -> dict:
    file = Path(path)
    if file.exists():
        data = load_json(file)
    else:
        data = {}

    if isinstance(data, dict):
        data[key] = value
        save_json(file, data)
        return data
    else:
        raise TypeError("JSON not dict!")
