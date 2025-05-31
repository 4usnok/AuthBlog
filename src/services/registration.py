import requests
from sqlalchemy.orm import sessionmaker

from src.database.init_db import engine
from src.database.models import Person
from src.security.hashing import secure_wrap


class Registration:

    async def work_reg(self):
        """Метод для регистрации"""
        input_mail = input("Введите почту: ")
        input_login = input("Введите логин: ")
        input_password = input("Введите пароль: ")
        hashed_password = secure_wrap(input_password)

        url = "http://localhost:8000/registration/"
        data = {
            "email": input_mail,
            "login": input_login,
            "password": hashed_password
        }
        response = requests.post(url, json=data)
        self.append_int_db(input_mail, input_login, hashed_password)
        return response.json()

    def append_int_db(self, input_mail, input_login, hashed_password):
        """Добавление данных пользователя в БД"""
        Session = sessionmaker(bind=engine)
        with Session() as session:
            new_user = Person(
                email=input_mail,
                login=input_login,
                password=hashed_password
            )
            session.add(new_user)
            return session.commit()

print(Registration().work_reg())