"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


@pytest.fixture
def number5():
    return Item("жопич", 50000, 2)


def test_calculate_total_price(number5):
    """На расчет суммы конкретного товара в магазине"""
    assert number5.calculate_total_price() == 100000


def test_apply_discount(number5):
    number5.pay_rate = 0.8
    number5.apply_discount()
    assert number5.price == 40000.0
