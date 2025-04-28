import firebase_admin
from firebase_admin import credentials
import os

# Obtener la ruta absoluta del script actual
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construir la ruta absoluta al archivo JSON
json_path = os.path.join(script_dir, "tutor-virtual-ia-fce-firebase-adminsdk-fbsvc-28ed75aef2.json")

cred = credentials.Certificate(json_path)
