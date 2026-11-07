from lesson4.formatters import format_list, format_price
from lesson4.utils import cube, is_even, square


def run():
    return {
        "squares": [square(x) for x in range(2, 5)],
        "cubes": [cube(x) for x in range(2, 5)],
        "evens": [x for x in range(1, 5) if is_even(x)],
        "price": format_price(123.321),
        "items": format_list(["булочки", "сгущенка", "кофе"]),
    }


if __name__ == "__main__":
    print(run())
