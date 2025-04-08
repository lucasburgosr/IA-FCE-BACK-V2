import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("../tutor-virtual-ia-fce-firebase-adminsdk-fbsvc-764b634a0a.json")
firebase_admin.initialize_app(cred)