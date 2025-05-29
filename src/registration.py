import requests


class Registration:

    def work_reg(self):
        """Метод для регистрации"""
        input_mail = input("Введите почту: ")
        input_login = input("Введите логин: ")
        input_password = input("Введите пароль: ")

        url = "http://localhost:8000/registration/"
        data = {
            "email": input_mail,
            "login": input_login,
            "password": input_password
        }
        response = requests.post(url, json=data)
        return response.json()
