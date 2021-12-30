from email_validator import EmailValidatorError, validate_email


def _validate_email(email):
    msg = ""
    valid = False
    try:
        valid = validate_email(email)
        # update the email var with a normalized value
        email = valid.email
        valid = True
    except EmailValidatorError as e:
        msg = str(e)
    return valid, msg, email
