from argon2 import PasswordHasher
from argon2.exceptions import VerifyMissmatchError

def generate_hash(pw_raw):
    ph = PasswordHasher()
    return ph.hash(pw_raw)

def verify_hash(pw_hash, pw_raw):
    ph = PasswordHasher()
    msg = ''
    try:
        verified = ph.verify(pw_hash, pw_raw)
    except VerifyMissmatchError:
        verified = False
        msg = "Invalid password"
    except Exception as e:
        verified = False
        msg = f'Unexpected error: \n{e}'
    return verified, msg