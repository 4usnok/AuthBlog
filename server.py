from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
account = []  # Хранилище данных в памяти

class UserCreate(BaseModel):
    email: str
    login: str
    password: str

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

@app.post("/authorization/")
def user_verification():
    """Авторизация пользователя"""
    pass

@app.get("/users")
def read_root():
    """Просмотр списка"""
    return {"account": account}
