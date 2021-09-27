import pyrebase

config_dict = {
  'apiKey': 'AIzaSyDBILV4m6JYBdtPdusBNUbK-y0iOrzp5qw',
  'authDomain': 'hsegogame.firebaseapp.com',
  'projectId': 'hsegogame',
  'storageBucket': 'hsegogame.appspot.com',
  'messagingSenderId': '69167159208',
  'appId': '1:69167159208:web:839b8e36d13a5e30696f9d',
  'measurementId': 'G-2ZNDE4K5NR',
  'databaseURL': ''
}

firebase_instance = pyrebase.initialize_app(config_dict)