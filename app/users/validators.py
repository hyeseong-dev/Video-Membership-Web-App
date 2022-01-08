<<<<<<< HEAD
from email_validator import EmailNotValidError, validate_email

def _validate_email(email):
    msg = ''
    valid = False
    try : 
=======
from email_validator import validate_email, EmailNotValidError


def _validate_email(email):
    msg = ""
    valid = False
    try:
>>>>>>> dfca13acd72a73f43e494b706157848627ec4d15
        valid = validate_email(email)
        # update the email var with a normalized value
        email = valid.email
        valid = True
    except EmailNotValidError as e:
        msg = str(e)
<<<<<<< HEAD
    return valid, msg, email
=======
    return valid, msg, email
>>>>>>> dfca13acd72a73f43e494b706157848627ec4d15
