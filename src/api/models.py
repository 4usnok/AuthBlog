from pydantic import BaseModel, EmailStr, validator, SecretStr
from fastapi import FastAPI


app = FastAPI()
account = []  # Хранилище данных в памяти

class UserCreate(BaseModel):
    email: EmailStr
    login: str
    password: SecretStr

    @validator("password")
    def valid_password(cls, v):
        """Валидация пароля"""
        password = v.get_secret_value()
        if len(password) < 8:
            raise ValueError("Минимум 8 символов")
        if not any(c.isupper() for c in password):
            raise ValueError("Должна быть хотя бы одна заглавная буква")
        if not any(c.isdigit() for c in password):
            raise ValueError("Должна быть хотя бы одна цифра")
        return v
