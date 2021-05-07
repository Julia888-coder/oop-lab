from product import Product
from client import Client


class StoreSystem:
    """
    Класс ИС
    """

    def __init__(self):
        """
        Конструктор класса
        """
        self.list_of_products_sold = []  # список продаваемых товаров
        self.list_of_ordered_products = []  # список заказанных товаров
        self.list_of_clients = []  # список клиентов, заказавших товары
        self.number_of_orders = 0  # количество заказов

    def is_product_in_stock(self, product_name: str) -> bool:
        """
        Проверить товар на наличие в интернет-магазине
        :param product_name: название товара
        :return: True - если есть в наличии, иначе - False
        """
        for product in self.list_of_products_sold:
            if product.get_name().strip().lower() == product_name.strip().lower():  # все регистры и без лишних символов
                return True
        return False

    def get_product(self, product_name: str) -> Product:
        """
        Получить товар по его названию (предварительно воспользовавшись методом is_product_in_stock())
        :param product_name: название товара
        :return: возвращает товар
        """
        for product in self.list_of_products_sold:  # ищем среди продаваемых товаров
            if product.get_name().strip().lower() == product_name.strip().lower():  # все регистры и без лишних символов
                return product

        for product in self.list_of_ordered_products:  # ищем среди заказанных товаров
            if product.get_name().strip().lower() == product_name.strip().lower():  # все регистры и без лишних символов
                return product

    def change_product_price(self, product_name: str, new_price: int):
        """
        Изменить стоимость товара (предварительно воспользовавшись методом is_product_in_stock())
        :param product_name: название товара
        :param new_price: новая стоимость товара
        """
        old_price = self.get_product(product_name).get_price()
        self.get_product(product_name).set_price(new_price)
        print(f"Цена товара «{product_name}» обновлена с {old_price} р. на {new_price} р.")

    def change_product_description(self, product_name: str, new_description: str):
        """
        Изменить описание товара (предварительно воспользовавшись методом is_product_in_stock())
        :param product_name: название товара
        :param new_description: новое описание товара
        """
        old_description = self.get_product(product_name).get_description()
        self.get_product(product_name).set_description(new_description)
        print(f"Описание товара «{product_name}» обновлено с «{old_description}» на «{new_description}»")

    def top_up_list_of_products_sold(self, new_product: Product):
        """
        Добавить товар new_product в список продаваемых товаров (предварительно воспользовавшись методом
        is_product_in_stock())
        :param new_product: новый товар
        """
        self.list_of_products_sold.append(new_product)
        print(f"Товар «{new_product.get_name()}» теперь в наличии!")

    def display_list_of_products_sold(self):
        """
        Отобразить список продаваемых товаров
        """
        if len(self.list_of_products_sold) > 0:
            print("Список продаваемых товаров:")
            for product in self.list_of_products_sold:
                print(f"— «{product.get_name()}»")
        else:
            print("Пока что в наличии нет товаров...")

    def display_list_of_ordered_products(self):
        """
        Отобразить список заказанных товаров
        """
        if len(self.list_of_ordered_products) > 0:
            print("Список заказанных товаров:")
            for product in self.list_of_ordered_products:
                print(f"— «{product.get_name()}»")
        else:
            print("Пока что ни 1 товар не заказали...")

    def is_client_in_list(self, last_name: str) -> bool:
        """
        Проверить клиента на наличие в базе ИС
        :param last_name: фамилия
        :return: True - если есть в базе ИС, иначе - False
        """
        for client in self.list_of_clients:
            if client.get_last_name() == last_name.strip():  # без лишних символов
                return True
        return False

    def get_client(self, last_name: str) -> Client:
        """
        Найти клиента по фамилии (предварительно воспользовавшись методом is_client_in_list())
        :param last_name: фамилия
        :return: искомый клиент
        """
        for client in self.list_of_clients:
            if client.get_last_name() == last_name.strip():  # без лишних символов
                return client

    def register_an_order(self, product_name: str, first_name: str, last_name: str):
        """
        Зарегистрировать заказ клиента (first_name last_name) на товар (product_name) (предварительно воспользовавшись
        методом is_product_in_stock())
        :param product_name: название заказываемого товара
        :param first_name: имя клиента
        :param last_name: фамилия клиента
        """
        if self.is_client_in_list(last_name):
            the_client = self.get_client(last_name)
        else:
            the_client = Client(first_name, last_name)
            self.list_of_clients.append(the_client)

        the_product = self.get_product(product_name)
        self.list_of_products_sold.remove(the_product)
        the_client.order_product(the_product)
        self.list_of_ordered_products.append(the_product)
        self.number_of_orders += 1

        print(f"Заказ №{self.number_of_orders} успешно зарегистрирован! Клиент {first_name} {last_name} заказал(-а) "
              f"товар «{the_product.get_name()}».")

    def display_list_of_clients(self):
        """
        Отобразить список всех клиентов
        """
        if len(self.list_of_clients) > 0:
            print("Список клиентов:")
            for client in self.list_of_clients:
                print(f"— {client.get_first_name()} {client.get_last_name()}")
        else:
            print("Пока что у интернет-магазина не было ни 1 клиента...")
