from passlib.hash import bcrypt

def secure_wrap(password: str) -> str:
    """Обёртка безопасности: превращает пароль в необратимый хеш"""
    return bcrypt.hash(password)  # Автоматическая соль + 12 раундов
