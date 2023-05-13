import pytest
from src.item import Item


@pytest.fixture
def item():
    return Item("Смартфон", 10000, 20)


def test_repr(item):
    assert item.__repr__() == "Item('Смартфон', 10000, 20)"


def test_sts(item):
    assert item.__str__() == 'Смартфон'


def test_calculate_total_price(item):
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.calculate_total_price() == 160000


def test_name_setter(item):
    assert item.name == "Смартфон"


def test_name_setter_exception(item):
    with pytest.raises(Exception) as exception:
        item.name = "СуперСмартфон"
        assert f"Длина наименования товара превышает 10 символов" == exception.value.args[0]


def test_load_file():
    assert Item.load_file("items.csv")[1]["name"] == "Ноутбук"


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    item1 = Item.all[0]
    item2 = Item.all[1]
    assert item1.name == "Смартфон"
    assert item1.price == 100
    assert item2.name == "Ноутбук"


@pytest.mark.parametrize("string, expected", [("5", 5), ("5.0", 5), ("5.5", 5)])
def test_string_to_number(string, expected):
    assert Item.string_to_number(string) == expected
