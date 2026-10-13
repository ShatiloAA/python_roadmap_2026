from lesson0.main import greet


def test_imple_name() -> None:
    assert greet("Tony") == "Hello, Tony"


def test_empty_name() -> None:
    assert greet("") == "Hello, "
