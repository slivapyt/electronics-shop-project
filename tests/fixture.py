import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def number5():
    return Item("жопич", 50000, 2)


@pytest.fixture
def create_temp_csv(tmp_path):
    csv_text = """name,price,quantity
item1,10,1
item2,20,2
"""
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_text)
    return csv_file


@pytest.fixture
def phone_test_inp():
    return Phone("iPhone 14", 120_000, 5, 2)
