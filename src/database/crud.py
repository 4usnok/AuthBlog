from getpass import getpass

from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker

from src.database.created_db import engine
from src.database.model import users
from src.safety.hashing import hashing_password

# Создание сессии, через которую будем работать с добавлением в БД
SessionLocal = sessionmaker(autoflush=False, bind=engine)
db = SessionLocal()

class ClassFromCrud:

    def __init__(self):
        self.db = db

    def add_to_db(self):
        # добавление в БД приложения
        mail = input("mail: ")
        login = input("login: ")
        password = input("password: ")

        # проверяем, есть ли уже такой пользователь в БД
        existing_login_mail = (
                db.query(users).filter((users.mail == mail)).first()
                or db.query(users).filter((users.login == login)).first()
        )

        # проверка на наличие повторяющихся данных(почты и логина)
        if existing_login_mail:
            print("Пользователь с таким login или mail уже зарегистрирован.")
        # проверка на корректность структуры электронной почты
        elif '@' not in mail or '.' not in mail.split('@')[-1]:
            print("Ошибка: Email должен быть вида name@domain.com")
        else:
            # хеширование пароля
            hashed_password = hashing_password(password)
            add_in_db = users(mail=mail, login=login, password=hashed_password)
            # добавляем в бд
            db.add(add_in_db)
            print("Регистрация успешно выполнена!")
            # сохраняем изменения
        return db.commit()

# приложение, которое ничего не делает
app = FastAPI()
