from abc import ABC

class MusicalInstrument(ABC):
    """
    Базовый класс для всех музыкальных инструментов
    Определяет общие атрибуты и поведение для всех типов инструментов
    Инкапсуляция: атрибуты сделаны непубличными для предотвращения
    прямого доступа извне и обеспечения контроля через свойства
    """

    def __init__(self, name: str, brand: str, price: float, year: int) -> None:
        """
        Инициализация музыкального инструмента

        Args:
        name: Название инструмента
        brand: Производитель
        price: Цена в рублях
        year: Год выпуска
        """
        self._name = name
        self._brand = brand
        self._price = price
        self._year = year

    def __str__(self) -> str:
        """Возвращает понятное для пользователя описание инструмента"""
        return f"{self._brand} {self._name} ({self._year} г.) - {self._price} руб."

    def __repr__(self) -> str:
        """Возвращает детальное представление для разработчиков"""
        return (f"{self.__class__.__name__}(name='{self._name}', "
                f"brand='{self._brand}', price={self._price}, year={self._year})")

    def play(self) -> str:
        """
        Базовый метод воспроизведения звука

        Returns:
        Строка с описанием звучания инструмента
        """
        return f"Играет {self._name}"

    def get_info(self) -> dict:
        """
        Возвращает полную информацию об инструменте

        Returns:
        Словарь с атрибутами инструмента
        """
        return {
            'name': self._name,
            'brand': self._brand,
            'price': self._price,
            'year': self._year
        }

    def update_price(self, new_price: float) -> None:
        """
        Обновляет цену инструмента

        Args:
        new_price: Новая цена (должна быть положительной)
        """
        if new_price > 0:
            self._price = new_price

class Guitar(MusicalInstrument):
    """
    Класс гитары, наследующийся от MusicalInstrument
    Добавляет специфические для гитар атрибуты: количество струн и тип
    """

    def __init__(self, name: str, brand: str, price: float, year: int,
                 strings_count: int = 6, guitar_type: str = "акустическая") -> None:
        """
        Расширение конструктора базового класса характерными для гитар атрибутами

        Args:
        name: Название гитары
        brand: Производитель
        price: Цена
        year: Год выпуска
        strings_count: Количество струн (по умолчанию 6)
        guitar_type: Тип гитары (акустическая, электрогитара и т.д.)
        """
        super().__init__(name, brand, price, year)
        self._strings_count = strings_count
        self._guitar_type = guitar_type

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для добавления специфической информации

        Returns:
        Расширенное описание гитары
        """
        base_str = super().__str__()
        return f"{base_str}, {self._guitar_type} гитара, {self._strings_count} струн"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ для включения всех атрибутов

        Returns:
        Детальное представление гитары для разработчиков
        """
        return (f"Guitar(name='{self._name}', brand='{self._brand}', "
                f"price={self._price}, year={self._year}, "
                f"strings_count={self._strings_count}, guitar_type='{self._guitar_type}')")

    def play(self) -> str:
        """
        Перегрузка метода play для гитары

        Причина перегрузки: звучание гитары отличается от общего звучания инструментов.
        Гитара имеет характерный тембр и способ звукоизвлечения

        Returns:
        Строка с описанием игры на гитаре
        """
        return f"Звучит {self._guitar_type} гитара {self._name}"

    def tune(self, tuning: str = "стандартный") -> str:
        """
        Новый метод, специфичный для гитар

        Args:
        tuning: Тип строя гитары

        Returns:
        Сообщение о настройке гитары
        """
        return f"Гитара {self._name} настроена в {tuning} строй"

    # Унаследованный метод (без изменений)
    def get_info(self) -> dict:
        """
        Расширение унаследованного метода для добавления специфических полей

        Returns:
        Словарь с полной информацией о гитаре
        """
        info = super().get_info()
        info.update({
            'strings_count': self._strings_count,
            'guitar_type': self._guitar_type
        })
        return info

class Piano(MusicalInstrument):
    """
    Класс пианино, наследующийся от MusicalInstrument

    Добавляет специфические для пианино атрибуты: тип и количество клавиш
    """

    def __init__(self, name: str, brand: str, price: float, year: int,
                 keys_count: int = 88, piano_type: str = "рояль") -> None:
        """
        Расширение конструктора для пианино

        Args:
        name: Название пианино
        brand: Производитель
        price: Цена
        year: Год выпуска
        keys_count: Количество клавиш
        piano_type: Тип пианино (рояль, пианино, цифровое)
        """
        super().__init__(name, brand, price, year)
        self._keys_count = keys_count
        self._piano_type = piano_type

    def __str__(self) -> str:
        """
        Перегрузка метода __str__ для пианино

        Returns:
        Описание пианино с учётом его особенностей
        """
        base_str = super().__str__()
        return f"{base_str}, {self._piano_type}, {self._keys_count} клавиш"

    def __repr__(self) -> str:
        """
        Перегрузка метода __repr__ для пианино

        Returns:
        Детальное представление пианино для разработчиков
        """
        return (f"Piano(name='{self._name}', brand='{self._brand}', "
                f"price={self._price}, year={self._year}, "
                f"keys_count={self._keys_count}, piano_type='{self._piano_type}')")

    def play(self) -> str:
        """
        Перегрузка метода play для пианино

        Причина перегрузки: звучание пианино отличается от общего звучания инструментов
        и имеет механический способ звукоизвлечения

        Returns:
        Строка с описанием игры на пианино
        """
        return f"Звучит {self._piano_type}: {self._name}"

    def press_key(self, key: str) -> str:
        """
        Новый метод, характерный для клавишных

        Args:
        key: Название нажатой клавиши

        Returns:
        Сообщение о нажатой клавише
        """
        return f"Нажата клавиша {key} на пианино {self._name}"

if __name__ == "__main__":
    # Пример использования

    guitar = Guitar("Stratocaster", "Fender", 85000, 2020,
                   strings_count=6, guitar_type="электрогитара")
    piano = Piano("Grand", "Yamaha", 450000, 2019,
                 keys_count=88, piano_type="рояль")

    print(guitar)
    print(guitar.play())
    print(guitar.tune())

    print(piano)
    print(piano.play())
    print(piano.press_key("До"))

    pass