import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
import os
from dotenv import load_dotenv

load_dotenv()
cred_path = os.getenv("./firebase/firebase-adminsdk.json")
cred = credentials.Certificate("./firebase/firebase-adminsdk.json")
firebase_admin.initialize_app

def verify_firebase_token(token):
    try:
        decode_token = auth.verify_id_token(token)
        return decode_token
    except Exception as e:
        print("Token verification failed:",e)
        return None