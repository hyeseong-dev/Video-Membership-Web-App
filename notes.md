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