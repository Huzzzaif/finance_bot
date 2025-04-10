import firebase_admin
from firebase_admin import credentials, firestore

#Path to the key
cred = credentials.Certificate("./firebase/firebase-adminsdk.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()