from src.item import Item


class MixinLanguage:

    def __init__(self, name, price, quantity, language="EN") -> None:
        """
        Создание экземпляра класса

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param language: Язык раскладки клавиатуры.
        """
        super().__init__(name, price, quantity)
        self.__language = language

    @property
    def language(self) -> str:
        return self.__language

    def change_lang(self) -> object:
        """
        Метод изменения языка клавиатуры
        """
        if self.__language == "EN":
            self.__language = "RU"
            return self

        else:
            self.__language = "EN"
            return self


class Keyboard(MixinLanguage, Item):
    pass