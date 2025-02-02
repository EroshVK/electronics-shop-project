import csv, os



class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    def __repr__(self) -> str:
        """
        Метод для отображения информации об объекте класса в режиме отладки
        """
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self) -> str:
        """
        Метод для отображения информации об объекте класса для пользователей
        """
        return f"{self.name}"

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @property
    def name(self) -> str:
        """
        Создает свойство name класса Item
        :return: Свойство name класса Item
        """
        return self.__name

    @name.setter
    def name(self, name) -> None:
        """
        Сеттер для private атрибута name
        :param name: Private атрибут name
        :return: None
        """
        if len(name) > 10:
            raise Exception(f"Длина наименования товара превышает 10 символов")
        else:
            self.__name: str = name

    @staticmethod
    def load_file(filename) -> list:
        """
        Получает данные из csv-файла
        :return: Список словарей из строк csv-файла
        """
        data = []

        filedir = os.path.dirname(os.path.abspath(__file__))

        try:
            with open(os.path.join(f'{filedir}', filename), 'r+', encoding='windows-1251') as csv_file:
                csv_reader = csv.DictReader(csv_file)

                for item in csv_reader:
                    data.append(item)
                return data
        except:
            raise FileNotFoundError(f"Отсутствует файл {filename}")

    @classmethod
    def instantiate_from_csv(cls) -> None:
        """
        Инициализирует экземпляры класса Item данными из файла src/items.csv
        """
        filename = 'items.csv'
        cls.all = []
        data = cls.load_file(filename)
        for line in data:
            try:
                cls(line['name'],
                    cls.string_to_number(line['price']),
                    cls.string_to_number(line['quantity']))
            except:
                raise InstantiateCSVError(f"Файл {filename} поврежден")

    @staticmethod
    def string_to_number(num_str):
        """
        Статический метод, возвращающий число из числа-строки.

        :param num_str: Число-строка.
        :return: Число.
        """
        if "." in num_str:
            str_to_float: float = float(num_str)
            str_to_int: int = int(str_to_float)
        else:
            str_to_int: int = int(num_str)
        return str_to_int

    def __add__(self, other) -> int:
        """
        Метод для сложения количества товара в магазине для класса Item
        """
        if issubclass(other.__class__, self.__class__):
            return self.quantity + other.quantity
        else:
            raise Exception


class InstantiateCSVError(Exception):
    pass
