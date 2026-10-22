def squares(nums: list[int]) -> list[int]:
    return [x * x for x in nums]


def evens(nums: list[int]) -> list[int]:
    return [x for x in nums if x % 2 == 0]


def word_lengths(words: list[str]) -> dict[str, int]:
    return {w: len(w) for w in words}


def letters(text: str) -> set[str]:
    return {ch.lower() for ch in text if ch.isalpha()}


def has_negative(nums: list[int]) -> bool:
    return any(x < 0 for x in nums)


def indexed(items: list[str]) -> list[tuple[int, str]]:
    return [(i, w) for i, w in enumerate(items)]


def combined(a: list[str], b: list[int]) -> list[tuple[str, int]]:
    return [(x, y) for x, y in zip(a, b)]
