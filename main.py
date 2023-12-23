# file: main.py
from admin import Admin
from employee import Employee
from client import Client
from user import User
from database import Database

def display_menu(user):
    if isinstance(user, Admin):
        print("1. Просмотреть всех сотрудников")
        print("2. Добавить нового сотрудника")
        print("3. Обновить данные сотрудника")
        print("4. Удалить сотрудника")
    elif isinstance(user, Employee):
        print("1. Просмотреть все товары")
        print("2. Добавить товар")
        print("3. Обновить данные товара")
        print("4. Удалить товар")
        print("5. Просмотреть все заказы")
    elif isinstance(user, Client):
        print("1. Просмотреть все товары")
        print("2. Добавить товар в заказ")
        print("3. Просмотреть свои заказы")
        print("4. Удалить заказ")
        print("5. Разместить заказ")

    print("0. Выйти")

def login_menu():
    while True:
        print("Выберите роль:")
        print("1. Администратор")
        print("2. Сотрудник")
        print("3. Клиент")
        print("0. Выйти")

        role_choice = input("Ваш выбор: ")
        if role_choice == '0':
            break

        login = input("Введите логин: ")
        password = input("Введите пароль: ")

        user = None

        if role_choice == '1':
            user = Admin("", "", login, password)
        elif role_choice == '2':
            user = Employee("", "", login, password)
        elif role_choice == '3':
            user = Client("", "", login, password)
        else:
            print("Неверный выбор роли. Пожалуйста, выберите снова.")
            continue

        if user.authenticate():
            print("Авторизация успешна!")
            while True:
                display_menu(user)
                choice = input("Выберите действие: ")

                if choice == '1':
                    user.view_all_employees() if isinstance(user, Admin) else user.view_products()
                elif choice == '2':
                    if isinstance(user, Admin):
                        user.add_employee()
                    elif isinstance(user, Employee):
                        user.add_product()
                    elif isinstance(user, Client):
                        user.add_product_to_cart()
                elif choice == '3':
                    if isinstance(user, Admin):
                        user.update_employee()
                    elif isinstance(user, Employee):
                        user.update_product()
                    elif isinstance(user, Client):
                        user.view_orders()
                elif choice == '4':
                    if isinstance(user, Admin):
                        user.delete_employee()
                    elif isinstance(user, Employee):
                        user.delete_product()
                    elif isinstance(user, Client):
                        user.delete_order()
                elif choice == '5':
                    if isinstance(user, Employee):
                        user.view_all_orders()
                    if isinstance(user, Client):
                        user.place_order()
                elif choice == '0':
                    break
                else:
                    print("Неверный выбор. Пожалуйста, выберите снова.")

def main():
    db = Database()
    db.create_tables()

    while True:
        print("1. Войти")
        print("2. Зарегистрироваться")
        print("0. Выйти")

        entry_choice = input("Ваш выбор: ")

        if entry_choice == '1':
            login_menu()
        elif entry_choice == '2':
            role_choice = input("Выберите роль (admin, employee, client): ")
            first_name = input("Введите ваше имя: ")
            last_name = input("Введите вашу фамилию: ")
            login = input("Введите логин: ")
            password = input("Введите пароль: ")

            if role_choice not in ['admin', 'employee', 'client']:
                print("Неверный выбор роли. Пожалуйста, выберите снова.")
                continue

            user = User(first_name, last_name, login, password, role_choice)
            user.register()
        elif entry_choice == '0':
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    main()
