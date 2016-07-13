import re



def valid_username(username):
    user_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return user_re.match(username)


def valid_password(password):
    pass_re = re.compile("^.{3,20}$")
    return pass_re.match(password)


def valid_email(email):
    email_re = re.compile("^[\S]+@[\S]+.[\S]+$")
    return email_re.match(email)