# TODO Написать 3 класса с документацией и аннотацией типов
import doctest

class Book:
    def __init__(self, title: str, author: str, page_count: int):
        """
        Создание и подготовка к работе объекта "Книга"

        :param title: Название книги
        :param author: Автор книги
        :param page_count: Количество страниц в книге

        Примеры:
        >>> book = Book("Война и мир", "Лев Толстой", 1300)
        """
        if not isinstance(title, str):
            raise TypeError("Название книги должно быть строкой")
        if not title.strip():
            raise ValueError("Название книги не может быть пустым")
        self.title = title

        if not isinstance(author, str):
            raise TypeError("Имя автора должно быть строкой")
        if not author.strip():
            raise ValueError("Имя автора не может быть пустым")
        self.author = author

        if not isinstance(page_count, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if page_count <= 0:
            raise ValueError("Количество страниц должно быть положительным числом")
        self.page_count = page_count

        self.current_page = 1
        self.is_open = False

    def open_book(self) -> None:
        """
        Открытие книги.

        :return: None

        Примеры:
        >>> book = Book("1984", "Джордж Оруэлл", 328)
        >>> book.open_book()
        """
        ...

    def turn_page(self, pages: int) -> None:
        """
        Перелистывание страниц.

        :param pages: Количество страниц для перелистывания (может быть отрицательным для листания назад)
        :raise ValueError: Если пытаемся перелистнуть больше страниц, чем есть в книге,
        или если текущая страница становится меньше 1

        :return: None

        Примеры:
        >>> book = Book("Мастер и Маргарита", "Михаил Булгаков", 480)
        >>> book.open_book()
        >>> book.turn_page(50)
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом")
        ...

    def get_current_page(self) -> int:
        """
        Получение номера текущей страницы.

        :return: Номер текущей страницы

        Примеры:
        >>> book = Book("Преступление и наказание", "Федор Достоевский", 672)
        >>> book.open_book()
        >>> book.get_current_page()
        """
        ...

class Smartphone:
    def __init__(self, brand: str, model: str, battery_level: float):
        """
        Создание и подготовка к работе объекта "Смартфон"

        :param brand: Производитель смартфона
        :param model: Модель смартфона
        :param battery_level: Уровень заряда батареи в процентах

        Примеры:
        >>> phone = Smartphone("Apple", "iPhone 15", 85.5)
        """
        if not isinstance(brand, str):
            raise TypeError("Производитель должен быть строкой")
        if not brand.strip():
            raise ValueError("Производитель не может быть пустым")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Модель должна быть строкой")
        if not model.strip():
            raise ValueError("Модель не может быть пустой")
        self.model = model

        if not isinstance(battery_level, (int, float)):
            raise TypeError("Уровень заряда должен быть числом")
        if battery_level < 0 or battery_level > 100:
            raise ValueError("Уровень заряда должен быть в диапазоне от 0 до 100")
        self.battery_level = battery_level

        self.is_on = False
        self.installed_apps = []

    def power_on(self) -> None:
        """
        Включение смартфона.

        :return: None

        Примеры:
        >>> phone = Smartphone("Samsung", "Galaxy S24", 100)
        >>> phone.power_on()
        """
        ...

    def install_app(self, app_name: str) -> None:
        """
        Установка приложения на смартфон.

        :param app_name: Название приложения
        :raise ValueError: Если приложение с таким названием уже установлено

        :return: None

        Примеры:
        >>> phone = Smartphone("Google", "Pixel 8", 90)
        >>> phone.install_app("Telegram")
        """
        if not isinstance(app_name, str):
            raise TypeError("Название приложения должно быть строкой")
        if not app_name.strip():
            raise ValueError("Название приложения не может быть пустым")
        ...

    def check_battery(self) -> float:
        """
        Проверка уровня заряда батареи.

        :return: Текущий уровень заряда в процентах

        Примеры:
        >>> phone = Smartphone("OnePlus", "12", 75)
        >>> phone.check_battery()
        """
        ...

class BankAccount:
    def __init__(self, account_number: str, owner_name: str, balance: float):
        """
        Создание и подготовка к работе объекта "Банковский счет"

        :param account_number: Номер банковского счета
        :param owner_name: Имя владельца счета
        :param balance: Текущий баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910000001", "Иван Петров", 50000.0)
        """
        if not isinstance(account_number, str):
            raise TypeError("Номер счета должен быть строкой")
        if not account_number.strip():
            raise ValueError("Номер счета не может быть пустым")
        if len(account_number) < 10:
            raise ValueError("Номер счета должен содержать минимум 10 символов")
        self.account_number = account_number

        if not isinstance(owner_name, str):
            raise TypeError("Имя владельца должно быть строкой")
        if not owner_name.strip():
            raise ValueError("Имя владельца не может быть пустым")
        self.owner_name = owner_name

        if not isinstance(balance, (int, float)):
            raise TypeError("Баланс должен быть числом")
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self.balance = balance

        self.is_active = True
        self.transaction_history = []

    def deposit(self, amount: float) -> float:
        """
        Внесение средств на счет.

        :param amount: Сумма для внесения
        :raise ValueError: Если сумма внесения меньше или равна нулю
        :return: Новый баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910000002", "Анна Сидорова", 10000.0)
        >>> account.deposit(5000.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма внесения должна быть положительной")
        ...

    def withdraw(self, amount: float) -> float:
        """
        Снятие средств со счета.

        :param amount: Сумма для снятия
        :raise ValueError: Если сумма снятия превышает текущий баланс,
        или если сумма снятия меньше или равна нулю

        :return: Новый баланс счета

        Примеры:
        >>> account = BankAccount("40817810099910000003", "Петр Иванов", 20000.0)
        >>> account.withdraw(5000.0)
        """
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете")
        ...

    def get_balance_info(self) -> str:
        """
        Получение информации о балансе счета.

        :return: Строка с информацией о балансе

        Примеры:
        >>> account = BankAccount("40817810099910000004", "Елена Николаева", 30000.0)
        >>> account.get_balance_info()
        """
        ...

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()