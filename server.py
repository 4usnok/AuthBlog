from fastapi import FastAPI

# Создание приложения
app = FastAPI()

@app.get("/")
def read_root():
    """Добавление главной страницы"""
    return {"регистрация": "http://127.0.0.1:8000/registration"}

@app.get("/registration")
def read_root():
    """Добавление страницы регистрации"""
    return {"message": "Привет, FastAPI!"}
