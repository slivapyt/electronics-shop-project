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
    '''тест на применение скидки'''
    number5.pay_rate = 0.8
    number5.apply_discount()
    assert number5.price == 40000.0


def test_name(number5):
    '''Длина строки name не больше 10 символов'''
    assert number5.name == "жопич"
    number5.name = "жопичжопичжопич"
    assert number5.name == "жопичжопич"


@pytest.fixture
def create_temp_csv(tmp_path):
    csv_text = """name,price,quantity
item1,10,1
item2,20,2
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_text)
    return csv_file


def test_instantiate_from_csv(create_temp_csv):
    csv_file = create_temp_csv
    items = Item.instantiate_from_csv(csv_file)
    assert len(items) == 2
    assert items[0].name == "item1"
    assert items[0].price == "10"
    assert items[0].quantity == "1"
    assert items[1].name == "item2"
    assert items[1].price == "20"
    assert items[1].quantity == "2"


def test_string_to_number():
    assert Item.string_to_number("3.7") == 3
    assert Item.string_to_number("6.1") == 6
    assert Item.string_to_number("9.9") == 9


def test__repr__(number5):
    assert number5.__repr__() == "Item('жопич', 50000, 2)"


def test__str__(number5):
    assert number5.__str__() == 'жопич'
