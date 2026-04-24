import bcrypt
import jwt
import datetime
from django.conf import settings


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def check_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed.encode('utf-8'))


def generate_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now(datetime.UTC) + datetime.timedelta(hours=settings.JWT_EXPIRATION_HOURS)
    }

    return jwt.encode(payload=payload, key=settings.JWT_SECRET_KEY, algorithm='HS256')


def decode_token(token):
    return jwt.decode(token, key=settings.JWT_SECRET_KEY, algorithms='HS256')
