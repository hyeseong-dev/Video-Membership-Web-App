import datetime
from jose import jwt, ExpiredSignatureError
from app import conf
from .models import User

settings = conf.get_settings()

def authenticate(email, password):
    try:
        user_obj = User.objects.get(email=email)
    except Exception as e:
        user_obj = None
    if not user_obj.verify_password(password):
        return None
    return user_obj

def login(user_obj, expires=5):
    raw_data = {
        'user_id': f"{user_obj.id}",
        'role': 'admin',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expires)
    }
    return jwt.encode(raw_data, settings.secret_key, algorithm=settings.jwt_algorithm)

def verify_user_id(token):
    data = None
    try:
        data = jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
    except ExpiredSignatureError as e:
        pass
    if 'user_id' not in data:
        return None
        print(e)
    return data