import pytest
from src.item import Item
from src.phone import Phone


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def phone1():
    return Phone("iPhone 14", 120000, 5, 2)


@pytest.fixture
def phone2():
    return Phone("iPhone 13", 70000, 7, 1)


def test_repr(phone1):
    assert phone1.__repr__() == "Phone('iPhone 14', 120000, 5, 2)"


def test_add(item, phone1, phone2):
    assert item + phone1 == 25
    assert phone1 + phone2 == 12


def test_number_of_sim_exception(phone1):
    with pytest.raises(ValueError):
        phone1.number_of_sim = 0
        phone1.number_of_sim = -1
