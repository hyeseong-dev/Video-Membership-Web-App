import uuid
from app.config import get_settings
from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model

from . import validators, securities

settings = get_settings()

class User(Model):
    __keyspace__ = settings.keyspace
    email = columns.Text(primary_key=True)
    user_id = columns.UUID(primary_key=True, default=uuid.uuid1)
    password = columns.Text()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return f"User(email={self.email}, user_id={self.user_id})"

    def set_password(self, raw_password, commit=False):
        hashed_password = securities.generate_hash(raw_password)
        self.password = hashed_password
        if commit:
            self.save()
        return True
        
    def verify_password(self, raw_password):
        hashed_password = self.password
        verified, _ = securities.verify_hash(hashed_password, raw_password)
        return verified

    @staticmethod
    def create_user(email, password=None):
        if (q := User.objects.filter(email=email)).count() != 0:
            raise Exception("User already has account")
        valid, msg, email = validators._validate_email((email))
        if not valid:
            raise Exception(f"Invalid email:{msg}")
        obj = User(email=email)
        obj.set_password(password)
        # obj.password = password
        obj.save()
        return obj
