from product import Product


class Client:
    """
    Класс клиента
    """

    def __init__(self, first_name: str, last_name: str):
        """
        Конструктор класса
        :param first_name: имя
        :param last_name: фамилия
        """
        self.first_name = first_name
        self.last_name = last_name
        self.list_of_ordered_products = []  # список заказанных товаров

    def get_first_name(self) -> str:
        """
        Получить имя клиента
        :return: имя клиента
        """
        return self.first_name

    def get_last_name(self) -> str:
        """
        Получить фамилию клиента
        :return: фамилия клиента
        """
        return self.last_name

    def order_product(self, product: Product):
        """
        Заказать товар
        :param product: заказываемый товар
        """
        self.list_of_ordered_products.append(product)

    def display_order_amount(self):
        """
        Отобразить суммарную стоимость заказанных клиентом товаров
        """
        order_amount = 0
        for product in self.list_of_ordered_products:
            order_amount += product.get_price()
        print(f"{self.first_name} {self.last_name} заказал(-а) товаров на {order_amount} р.")

    def display_list_of_ordered_products(self):
        """
        Отобразить список товаров, заказанных клиентом
        """
        list_of_ordered_products_str = f"Товары, которые заказал(-а) {self.first_name} {self.last_name}: "
        for product in self.list_of_ordered_products:
            list_of_ordered_products_str += product.get_name() + " "
        print(list_of_ordered_products_str)
