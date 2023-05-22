import pytest
from src.keyboard import Keyboard


@pytest.fixture
def keyboard():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(keyboard):
    assert keyboard.language == "EN"
    keyboard.change_lang()
    assert keyboard.language == "RU"
    keyboard.change_lang()
    assert keyboard.language == "EN"

    with pytest.raises(AttributeError):
        keyboard.language = "CH"
        keyboard.language = 1
