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
    result = []
    for i, w in enumerate(words):
        result.append((i, w))
    return result


def unique_words(text: str) -> list[str]:
    words = text.lower().split()
    unique: dict = {w: w for w in words}
    return list(unique)
