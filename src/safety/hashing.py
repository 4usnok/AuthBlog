import bcrypt

def hashing_password(hashing):
    return bcrypt.hashpw(hashing.encode(), bcrypt.gensalt())
