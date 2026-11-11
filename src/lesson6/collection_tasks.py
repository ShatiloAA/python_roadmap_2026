from collections import Counter, defaultdict


def unique_in_order(items: list[str]) -> list[str]:
    """Убрать дубли, сохранив порядок первого появления."""
    unique_dict = dict.fromkeys(items)
    return [k for k in unique_dict]


def common_elements(a: list[int], b: list[int]) -> set[int]:
    """Пересечение двух списков как set"""
    unique_a = {item for item in a}
    unique_b = {item for item in b}
    return unique_a & unique_b


def count_chars(text: str) -> dict[str, int]:
    """Частота каждого символа (пробелы и знаки тоже считаем)."""
    return Counter(text)


def group_by_length(words: list[str]) -> dict[int, list[str]]:
    """Сгруппировать слова по длине, порядок слов сохранить, ключи — по возрастанию длины."""
    result = defaultdict(list)
    for w in words:
        result[len(w)].append(w)
    return result


# TODO
def is_anagram(a: str, b: str) -> bool:
    """Анаграммы ли строки (игнорируя регистр и пробелы)."""
    return False


# TODO
def pairs_to_dict(pairs: list[tuple[str, int]]) -> dict[str, int]:
    """Превратить список пар в словарь. Если ключ повторяется — последнее значение побеждает."""

    return {}
