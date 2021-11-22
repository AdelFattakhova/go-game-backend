import pyrebase
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

config_dict = {
  'apiKey': 'AIzaSyDBILV4m6JYBdtPdusBNUbK-y0iOrzp5qw',
  'authDomain': 'hsegogame.firebaseapp.com',
  'projectId': 'hsegogame',
  'storageBucket': 'hsegogame.appspot.com',
  'messagingSenderId': '69167159208',
  'appId': '1:69167159208:web:839b8e36d13a5e30696f9d',
  'measurementId': 'G-2ZNDE4K5NR',
  'databaseURL': 'https://hsegogame-default-rtdb.firebaseio.com'
}

firebase_instance = pyrebase.initialize_app(config_dict)

config = Config('.env')
oauth = OAuth(config)

CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
oauth.register(
    name='google',
    server_metadata_url=CONF_URL,
    client_kwargs={
        'scope': 'openid email profile'
    }
)
