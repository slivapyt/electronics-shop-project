import csv
import math


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0

    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        name: Название товара.
        price: Цена за единицу товара.
        quantity: Количество товара в магазине.
        """
        super().__init__()
        self.__name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * self.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        if len(self.__name) == 10:
            return self.__name
        else:
            self.__name = self.__name[:10]
            return self.__name

    @classmethod
    def instantiate_from_csv(cls, read_file):
        with open(read_file, 'r', encoding='cp1251') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                if row[0] != 'name':
                    name, price, quantity = row
                    item = cls(name, price, quantity)
                    cls.all.append(item)
        return cls.all

    @staticmethod
    def string_to_number(num):
        return math.floor(float(num))

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.quantity + other.quantity

        raise Exception

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.__name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        return f'{self.name}'
