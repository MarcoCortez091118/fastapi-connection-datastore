import firebase_admin
from firebase_admin import credentials, firestore
from app.core.config import settings
import json

class Firebase:
    def __init__(self):
        if not firebase_admin._apps:  # Evitar inicialización múltiple
            cred = credentials.Certificate(json.loads(settings.GOOGLE_APPLICATION_CREDENTIALS))
            firebase_admin.initialize_app(cred)
        self.db = firestore.client()

    def get_db(self):
        return self.db

firebase = Firebase()
