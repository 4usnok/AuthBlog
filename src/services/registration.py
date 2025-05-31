import asyncio
import aiohttp
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from src.security.hashing import secure_wrap
from src.database.models import Person


class Registration:
    def __init__(self):
        self.engine = create_async_engine(
            "postgresql+asyncpg://user:pass@localhost/db",
            pool_pre_ping=True,
            echo=True
        )
        self.async_session = async_sessionmaker(
            bind=self.engine,
            expire_on_commit=False
        )

    async def work_reg(self):
        input_mail = input("Введите почту: ")
        input_login = input("Введите логин: ")
        input_password = input("Введите пароль: ")

        try:
            hashed_password = secure_wrap(input_password)
        except Exception as e:
            print(f"Ошибка хеширования: {e}")
            return

        # HTTP запрос
        async with aiohttp.ClientSession() as http_session:
            try:
                async with http_session.post(
                        "http://localhost:8000/registration/",
                        json={
                            "email": input_mail,
                            "login": input_login,
                            "password": hashed_password
                        },
                        timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    result = await response.json()
            except Exception as e:
                print(f"Ошибка HTTP запроса: {e}")
                return

        # Сохранение в БД
        try:
            await self.append_int_db(input_mail, input_login, hashed_password)
        except Exception as e:
            print(f"Ошибка сохранения в БД: {e}")
            return

        return result

    async def append_int_db(self, email, login, password):
        async with self.async_session() as session:
            try:
                session.add(Person(
                    email=email,
                    login=login,
                    password=password
                ))
                await session.commit()
            except:
                await session.rollback()
                raise


async def main():
    reg = Registration()
    result = await reg.work_reg()
    print(result)


if __name__ == "__main__":
    asyncio.run(main())