from product import Product
from system import StoreSystem


def get_started_with_online_store():
    """
    Начать работу с интернет-магазином
    """
    the_online_store_system = StoreSystem()
    print("Информационная система интернет-магазина успешно работает! Напишите:"
          "\n— «1», если Вы хотите приступить к работе с товарами;"
          "\n— «2», если Вы хотите приступить к работе с покупателями;"
          "\n— «-1», если Вы хотите завершить работу информационной системы.")

    command = input("Введите команду: ")
    while command != "-1":
        if command == "1":
            print("Напишите:"
                  "\n— «4», если Вы хотите пополнить список продаваемых товаров;"
                  "\n— «5», если Вы хотите вывести товары, заказанные клиентами;"
                  "\n— «6», если Вы хотите вывести товары, доступные для покупки;"
                  "\n— «7», если Вы хотите изменить цену определённого товара;"
                  "\n— «8», если Вы хотите изменить описание определённого товара;"
                  "\n— «9», если Вы хотите узнать больше о конкретном товаре.")
        elif command == "2":
            print("Напишите:"
                  "\n— «10», если Вы хотите зарегистрировать заказ клиента;"
                  "\n— «11», если Вы хотите вывести список товаров, заказанных клиентом;"
                  "\n— «12», если Вы хотите вывести сумму заказа клиента;"
                  "\n— «13», если Вы хотите вывести список всех клиентов.")
        elif command == "3":
            print("Напишите:"
                  "\n— «1», если Вы хотите приступить к работе с товарами;"
                  "\n— «2», если Вы хотите приступить к работе с покупателями;"
                  "\n— «-1», если Вы хотите завершить работу информационной системы.")
        elif command == "4":
            the_product_name = input("Введите название товара: ")
            if the_online_store_system.is_product_in_stock(the_product_name):
                print(f"Товар «{the_product_name}» уже в наличии!")
            else:
                if len(the_product_name) != 0:
                    the_product_price = int(input(f"Введите цену товара «{the_product_name}»: "))
                    the_product_description = input(f"Введите описание товара «{the_product_name}»: ")
                    the_product = Product(the_product_name, the_product_price, the_product_description)
                    the_online_store_system.top_up_list_of_products_sold(the_product)
                else:
                    print("Некорректный ввод названия товара!")
        elif command == "5":
            the_online_store_system.display_list_of_ordered_products()
        elif command == "6":
            the_online_store_system.display_list_of_products_sold()
        elif command == "7":
            product_name = input("Введите название товара: ")
            if the_online_store_system.is_product_in_stock(product_name):
                new_price = int(input(f"Введите новую цену товара «{product_name}»: "))
                the_online_store_system.change_product_price(product_name, new_price)
            else:
                print(f"Товар «{product_name}» не существует!")
        elif command == "8":
            product_name = input("Введите название товара: ")
            if the_online_store_system.is_product_in_stock(product_name):
                new_description = input(f"Введите новое описание товара «{product_name}»: ")
                the_online_store_system.change_product_description(product_name, new_description)
            else:
                print(f"Товар «{product_name}» не существует!")
        elif command == "9":
            product_name = input("Введите название товара: ")
            if the_online_store_system.is_product_in_stock(product_name):
                the_online_store_system.get_product(product_name).display_full_information()
            else:
                print(f"Товар «{product_name}» не существует!")
        elif command == "10":
            product_name = input("Введите название товара: ")
            if the_online_store_system.is_product_in_stock(product_name):
                first_name = input("Введите имя клиента: ")
                last_name = input("Введите фамилию клиента: ")
                if len(first_name) > 0 and len(last_name) > 0:
                    the_online_store_system.register_an_order(product_name, first_name, last_name)
                else:
                    print("Некорректный ввод персональных данных!")
            else:
                print(f"Не удалось зарегистрировать заказ: товара «{product_name}» нет в наличии!")
        elif command == "11":
            last_name = input("Введите фамилию клиента: ")
            if the_online_store_system.is_client_in_list(last_name):
                the_client = the_online_store_system.get_client(last_name)
                the_client.display_list_of_ordered_products()
            else:
                print(f"Человек с фамилией «{last_name}» не заказывал товары в нашем интернет-магазине!")
        elif command == "12":
            last_name = input("Введите фамилию клиента: ")
            if the_online_store_system.is_client_in_list(last_name):
                the_client = the_online_store_system.get_client(last_name)
                the_client.display_order_amount()
            else:
                print(f"Человек с фамилией «{last_name}» не заказывал товары в нашем интернет-магазине!")
        elif command == "13":
            the_online_store_system.display_list_of_clients()
        elif command == "-1":
            print("Работа информационной системы интернет-магазина завершена!")
            return
        else:
            print("Некорректная команда! Повторите попытку! (Напишите «3», чтобы узнать список доступных команд)")

        command = input("Введите команду: ")

    print("Работа информационной системы интернет-магазина завершена!")


if __name__ == '__main__':
    get_started_with_online_store()