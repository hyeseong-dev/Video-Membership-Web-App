from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def generate_hash(raw_password):
    password = PasswordHasher()
    return password.hash(raw_password)

def verify_hash(hashed_password, raw_password):
    password = PasswordHasher()
    verified = False
    msg = ""
    try:
        verified = password.verify(hashed_password, raw_password)
    except VerifyMismatchError:
        verified = False
        msg = "Invalid password"
    except Exception as e:
        verified = False
        msg = f'Unexpected error: \n{e}'
    return verified, msg