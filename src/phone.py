from src.item import Item


class Phone(Item):

    def __init__(self, __name, price, quantity, number_of_sim):
        super().__init__(__name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self):
        old_rep = super().__repr__()
        return f"{old_rep[:-1]}, {str(self.number_of_sim)})"
