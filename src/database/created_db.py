from sqlite3 import OperationalError

from sqlalchemy import create_engine

from src.database.model import Base

# строка подключения
SQLALCHEMY_DATABASE_URL = "sqlite:///data/accounts.db"

# создаем движок SqlAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
# создаем таблицы
try:
    Base.metadata.create_all(bind=engine)
    print("Создание таблицы успешно!")
except OperationalError:
    print("Ошибка создания таблицы")
