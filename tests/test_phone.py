from tests.fixture import phone_test_inp


def test__repr__(phone_test_inp):
    print(phone_test_inp.__repr__())
    assert phone_test_inp.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_init_atr(phone_test_inp):
    assert phone_test_inp.name == 'iPhone 14'
    assert phone_test_inp.price == 120000
    assert phone_test_inp.quantity == 5
    assert phone_test_inp.number_of_sim == 2
