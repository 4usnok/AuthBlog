from sqlalchemy.orm import DeclarativeBase, validates
from sqlalchemy import Column, Integer, String

# создаем базовый класс для моделей
class Base(DeclarativeBase): pass

# создаем модель, объекты которой будут храниться в бд
class users(Base):
    """Создание таблицы с аккаунтами"""
    __tablename__ = "accounts"

    id = Column(Integer, primary_key=True, index=True)
    mail = Column(String)
    login = Column(String)
    password = Column(String)

    @validates("password")
    def validate_password(self, key, password):
        """Валидация пароля"""
        if len(password) < 8:
            raise ValueError("Пароль должен быть минимум 8 символов")
        return password
