from util.firebase import firebase_instance

auth = firebase_instance.auth()


def signup(email: str, password: str):
    return auth.create_user_with_email_and_password(email=email, password=password)


def login(email: str, password: str):
    return auth.sign_in_with_email_and_password(email=email, password=password)
