1. Video
 - Host -> Youtube - Private Video -> Udacity
        -> Vimeo, Wistia
        -> self hosted - nginx
 - Analytics
        - Lots of data
        - 1 user atches for 10 seconds on 100 viedos *
        - Lot of writes
        - Frame by Frame analysis -> 30 FPS -> 120 Seconds
        -> 3600cc

2. Members
 - Sign up
 - Login
 - Rember things
 - Email Validation / Confirmation


- Database name
    - Keyspace name 
        - Tables
    - Keyspace name A
        - Table A 
        - Table B 
        - Table C 

- Database for Testing
    - keyspace -> project 1
        - tables (correspond to prod)


```
User.create_user
```

```python
from app import db
from app.users.models import User
from cassandra.cqlengine.management import sync_table

db.get_session()
sync_table(User)

```

```python
## User Data Validation with pydantic
from app import db
from app.users.models import User
from cassandra.cqlengine.management import sync_table

db.get_session()
sync_table(User)

post_data = {'email': 'abc@abc.com', 'password': 'abc123'}

from pydantic import BaseModel, EmailStr, SecretStr, validator

class UserLoginSchema(BaseModel):
    email: EmailStr 
    password: SecretStr 

UserLoginSchema(**post_data)

class UserSignupSchema(BaseModel):
    email: EmailStr 
    password: SecretStr 
    password_confirm: SecretStr 

    @validator('email')
    def email_available(cls, v, values, **kwargs):
        q = User.objects.filter(email=v)
        if q.count() != 0:
            raise ValueError('Email is not available')
        return v

    @validator("password_confirm")
    def passwords_match(cls, v, values, **kwargs):
        password = values.get('password')
        password_confirm = v
        if password != password_confirm:
            raise ValueError("Passwords do not match")
        return v


data = UserSignupSchema(email='abc@gmail.com', password='abc123', password_confirm='abc123')
data.dict()
data.json()
data.dict()['password']
data.dict()['password'].get_secret_value()
```


```python
import datetime
import secrets
from jose import jwt

secret_key = secrets.token_urlsafe(50)
secret_key

algo = "HS256"

expires_after = 10

raw_data = {
    "user_id":'abc123',
    "role": "admin",
    "email": "do not do this",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_after)
}
encode_token = jwt.encode(raw_data, secret_key)
encode_token = jwt.encode(raw_data, secret_key, algorithm=algo)

j = User.objects.filter(raw_data, secret_key, algorithm=algo)

def login(user_id, expires=5):
    try : 
        raw_data = {
            "user_id":'abc123',
            "role": "admin",
            "email": "do not do this",
            "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=expires_after)
        }
        return jwt.decode(encode_token, secret_key, algorithms=[algo])
    except ExpiredSignatureError as e:
        print(e)

token = login(j.user_id, expires=5)
token


def verify_user(token):
    data = None
    verified = False
    try:
        data = jwt.decode(token, secret_key, algorithms=[algo])
        verified = True
    except ExpiredSignatureError as e:
        print(e)
    except :
        pass
    return data, verified

verify_user(token)
```