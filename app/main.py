from fastapi import FastAPI

from cassandra.cqlengine.management import sync_table

from . import config, db
from app.users.models import User

app = FastAPI()
# settings = config.get_settings()

@app.on_event('startup')
def on_startup():
    # triggered when fastapi starts
    print('hello world')
    DB_SESSION = db.get_session()
    sync_table(User)



@app.get('/')
def homepage():
    return dict(hello='world',)

@app.get('/users')
def users_list_view():
    q = User.objects.all().limit(10)
    return list(q)