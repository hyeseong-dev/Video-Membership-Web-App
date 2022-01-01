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