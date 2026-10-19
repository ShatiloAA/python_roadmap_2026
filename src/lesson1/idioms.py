from collections import Counter


def top_words(text: str, n: int = 3) -> list[tuple[str, int]]:
    arr = text.lower().split()
    freq = Counter(arr)
    result = sorted(freq.items(), key=lambda v: (-v[1], v[0]))

    return result[:n]


def is_palindrome(text: str) -> bool:
    str_arr = [x.lower() for x in text if x.isalpha()]
    clean_str = "".join(str_arr)
    return clean_str == clean_str[::-1]


def index_words(text: str) -> list[tuple[int, str]]:
    words = text.lower().split()
    result = [(i, w) for i, w in enumerate(words)]
    return result


def unique_words(text: str) -> list[str]:
    words = text.lower().split()
    unique: dict[str, None] = dict.fromkeys(words)
    return list(unique)
