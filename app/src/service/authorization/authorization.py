from requests import HTTPError
import json

from util.json_base import Generic
from util.firebase import firebase_instance

auth = firebase_instance.auth()


def signup(email: str, password: str):
    try:
        return auth.create_user_with_email_and_password(email=email, password=password)
    except HTTPError as e:
        handle_http_error(e)


def login(email: str, password: str):
    try:
        return auth.sign_in_with_email_and_password(email=email, password=password)
    except HTTPError as e:
        handle_http_error(e)


def restore_password(email: str):
    try:
        return auth.send_password_reset_email(email=email)
    except HTTPError as e:
        handle_http_error(e)


def handle_http_error(error: HTTPError):
    response = json.loads(error.args[0].response.text, object_hook=Generic.from_dict)
    raise HTTPError(response.error.code, response.error.message)
