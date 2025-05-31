from fastapi import FastAPI
from .models import UserCreate

app = FastAPI()
account = []  # Хранилище данных в памяти

@app.post("/registration/")
def creation_account(user: UserCreate):
    """Регистрация нового пользователя"""
    if user not in account:
        account.append({
            "email": user.email,
            "login": user.login,
            "password": user.password
        })
        return {"message": f"Регистрация прошла успешно!"}

@app.get("/users")
def read_root():
    """Просмотр списка"""
    return {"account": account}