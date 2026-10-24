def safe_divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Попытка деления на ноль!")
    else:
        return a / float(b)


def parse_int(s: str) -> int:
    try:
        return int(s)
    except ValueError as e:
        raise ValueError("Строка не может быть приведена к int!") from e


def validate_age(age: int) -> int:
    if age < 0 or age > 150:
        raise ValueError("Некорректный возраст!")
    else:
        return age


class NotPositiveError(Exception):
    pass


def validate_positive(name: str, value: int) -> int:
    if value <= 0:
        raise NotPositiveError(f"{name} must be positive!")
    return value
