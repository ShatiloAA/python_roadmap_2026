def format_price(price: float) -> str:
    return f"{price:.2f} ₽"


def format_list(items: list[str]) -> str:
    if len(items) == 0:
        return ""
    return ", ".join(items)
