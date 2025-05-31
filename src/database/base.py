from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import DeclarativeBase


# путь, куда будет сохранена БД
DATABASE_URL = "sqlite+aiosqlite:///../../data/db_app.db"
# создание движка
engine = create_async_engine(DATABASE_URL)

class Base(DeclarativeBase):
    pass
