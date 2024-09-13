from example import check_correct
import pytest


@pytest.mark.parametrize("input_value, expected", [
    ("123", True),  # только цифры
    ("123abc", False),  # буквы
    ("", False),  # пустая строка
    ("456.78", False),  # содержит точку
    ("7890", True),  # только цифры
])
def test_check_correct(input_value, expected):
    assert check_correct(input_value) == expected


def test_1():
    assert 1 == 1
