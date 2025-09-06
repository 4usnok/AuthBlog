import bcrypt

def hashing_password(hashing):
    """Хеширование пароля"""
    return bcrypt.hashpw(hashing.encode(), bcrypt.gensalt())
