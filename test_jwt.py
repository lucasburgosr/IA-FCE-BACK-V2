# test_jwt.py
import os
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv

load_dotenv()
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"

if not JWT_SECRET_KEY:
    print("JWT_SECRET_KEY no está definido")
    exit(1)

payload = {
    "sub": "test@example.com",
    "exp": datetime.utcnow() + timedelta(minutes=60)
}

try:
    # Firmar el token
    token = jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)
    print("Token generado:", token)

    # Decodificar el token
    decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
    print("Token decodificado:", decoded)
except JWTError as e:
    print("Error al firmar o decodificar el token:", e)
