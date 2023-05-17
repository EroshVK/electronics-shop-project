from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim: int):
        """
        Создание экземпляра класса Phone.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        :param number_of_sim: Количество поддерживаемых сим-карт.
        """
        super().__init__(name, price, quantity)
        self.number_of_sim = number_of_sim

    def __repr__(self) -> str:
        """
        Переопределенный метод для отображения информации об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"

    def __add__(self, other) -> int:
        """
        Метод для сложения количества товара в магазине для класса Phone
        """
        if issubclass(self.__class__, other.__class__):
            return self.quantity + other.quantity
        else:
            raise Exception

    @property
    def number_of_sim(self):
        return self._number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, number):
        """ Добавляет проверку передаваемого значения"""
        if number <= 0 or not isinstance(number, int):
            raise ValueError("Количество физических SIM-карт должно быть целым числом больше нуля.")
        else:
            self._number_of_sim = number