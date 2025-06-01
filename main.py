import sqlite3

from src.database.crud import ClassFromCrud

class_obj = ClassFromCrud()
print(class_obj.add_to_db())

input_select = input("Посмотреть содержимое БД?: ")
if input_select.lower() == "Да".lower():
    connection = sqlite3.connect('data/accounts.db')
    cursor = connection.cursor()
    # Выбираем всех пользователей
    cursor.execute('SELECT * FROM accounts')
    users = cursor.fetchall()

    # Выводим результаты
    for user in users:
        print(user)

    # Закрываем соединение
    connection.close()
elif input_select.lower() == "Нет".lower():
    pass