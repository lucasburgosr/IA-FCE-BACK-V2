import os
import httpx
import asyncio
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from firebase_admin import auth
from models.alumno import Alumno
from datetime import datetime, timezone, timedelta
from jose import jwt
from repositories.usuario_repository import UsuarioRepository
from schemas.login_schema import LoginInput

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")  # Si lo necesitas para otros fines
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.usuario_repo = UsuarioRepository(db)

    async def registrar_alumnos(self, register_data: dict) -> dict:

        endpoint_verificacion = "http://dashboard.fce.uncu.edu.ar:5000/alutivos/verificaralumnotutor"

        dni = register_data.get("dni")

        payload = {"documento": dni}
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                endpoint_verificacion, 
                json=payload,
                headers={"Content-Type": "application/json"}
            )
        
        if response.status_code != 201:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Debes ser alumno/a de la FCE para registrarte"
            )
        
        data = response.json()
        if not data or not isinstance(data, list):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Respuesta de verificación inválida"
            )
        
        alumno_info = data[0]
        if alumno_info.get("claustro") != "EST" or alumno_info.get("calidad") != "A":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="No estás habilitado/a para registrarte en el Tutor"
            )
        
        try:
            firebase_user = await asyncio.to_thread(auth.create_user, email=register_data.get("email"), password=register_data.get("password"))
            firebase_uid = firebase_user.uid
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al crear usuario en Firebase: {str(e)}"
            )
        
        try:

            existing_user = self.usuario_repo.get_by_email(alumno_info.get("email"))
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="Ya estás registrado en el Tutor. Inicia sesión."
                )
            
            alumno = {
            "nombres": register_data.get("nombres"),
            "apellido": register_data.get("apellido"),
            "email": register_data.get("email"),
            "nro_documento": register_data.get("dni"),
            "contrasena": register_data.get("password"),
            "firebase_uid": firebase_uid
            }

            self.usuario_repo.create(alumno)
            self.db.commit()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al registrar el usuario en la base de datos: {str(e)}"
            )
        
        return {
            "message": "Usuario registrado exitosamente",
            "firebase_uid": firebase_uid,
            "email": alumno.get("email")
        }
    
    async def iniciar_sesion(self, login_data: LoginInput) -> dict:
        
        firebase_url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_API_KEY}"

        payload = {
            "email": login_data.email,
            "password": login_data.password,
            "returnSecureToken": True
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(firebase_url, json=payload)

        if response.status_code != 200:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Tu mail o contraseña son incorrectos"
            )
        
        firebase_data = response.json()
        firebase_uid = firebase_data.get("localId")

        usuario = self.usuario_repo.get_by_email(email=login_data.email)

        if not usuario:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No estás registrado como usuario. Regístrate para poder iniciar sesión."
            )
        
        update_data = {
            "firebase_uid": firebase_uid
        }

        self.usuario_repo.update(usuario=usuario, update_data=update_data)

        expire = datetime.now(timezone.utc).replace(tzinfo=None) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        payload_jwt = {"sub": usuario.email, "exp": expire}
        """ access_token = jwt.encode(payload_jwt, JWT_SECRET_KEY, algorithm=ALGORITHM) """

        return {
            "token": firebase_data.get("idToken"),
            "usuario_id": usuario.id,
            "email_usuario": usuario.email
        }
    
