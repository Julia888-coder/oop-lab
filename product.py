class Product:
    """
    Класс товара
    """

    def __init__(self, name: str, price: int, description: str):
        """
        Конструктор класса
        :param name: название товара
        :param price: стоимость товара
        :param description: описание товара
        """
        self.name = name.strip()  # .strip() - убираем лишние символы из названия
        self.price = price
        self.description = description

    def get_name(self) -> str:
        """
        Получить название товара
        :return: название товара
        """
        return self.name

    def get_price(self) -> int:
        """
        Получить стоимость товара
        :return: стоимость товара
        """
        return self.price

    def set_price(self, new_price: int):
        """
        Установить новую стоимость товару
        :param new_price: новая стоимость
        """
        self.price = new_price

    def get_description(self) -> str:
        """
        Получить описание товара
        :return: описание товара
        """
        return self.description

    def set_description(self, new_description: str):
        """
        Установить новое описание товара
        :param new_description: новое описание
        """
        self.description = new_description

    def display_full_information(self):
        """
        Отобразить полную информацию о товаре
        """
        print(f"Название товара: {self.name}\n"
              f"Цена товара: {self.price} р.\n"
              f"Описание товара: {self.description}")
