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

        # хеширование пароля
        hashed_password = hashing_password(password)

        add_in_db = users(mail=mail, login=login, password=hashed_password)
        db.add(add_in_db)     # добавляем в бд
        print("Регистрация успешно выполнена!")
        return db.commit()     # сохраняем изменения

# приложение, которое ничего не делает
app = FastAPI()
