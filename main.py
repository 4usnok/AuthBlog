import sqlite3

from src.services.registration import Registration

def main():
    # Подключение к базе
    conn = sqlite3.connect('data/db_app.db')
    cursor = conn.cursor()

    # Просмотреть содержимое таблицы accounts
    cursor.execute("SELECT * FROM accounts;")
    data = cursor.fetchall()

    # Закрываем соединение
    cursor.close()
    conn.close()
    return Registration().work_reg(), "Данные accounts: " + str(data)


if __name__ == "__main__":
    print(main())