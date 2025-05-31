import asyncio

from src.database.base import engine, Base


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

if __name__ == "__main__":
    print("Таблица создана!")
    asyncio.run(create_tables())