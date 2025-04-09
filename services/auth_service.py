import os
import httpx
import asyncio
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from firebase_admin import auth
from models.alumno import Alumno
from repositories.alumno_repository import AlumnoRepository

FIREBASE_API_KEY = os.getenv("FIREBASE_API_KEY")  # Si lo necesitas para otros fines

class AuthService:
    def __init__(self, db: Session):
        self.db = db
        self.alumno_repo = AlumnoRepository(db)

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
                detail="Error al verificar DNI"
            )
        
        data = response.json()
        if not data or not isinstance(data, list):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Respuesta de verificación inválida"
            )
        
        alumno_info = data[0]
        if alumno_info.get("claustro") != "EST" or alumno_info.get("calidad") != "A" or alumno_info.get("legajo") is not None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El alumno no cumple con los criterios de verificación"
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

            existing_user = self.alumno_repo.get_by_email(alumno_info.get("email"))
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="El usuario ya está registrado"
                )
            
            alumno = {
            "nombres": register_data.get("nombres"),
            "apellido": register_data.get("apellido"),
            "email": register_data.get("email"),
            "nro_documento": register_data.get("dni"),
            "contrasena": register_data.get("password"),
            "firebase_uid": firebase_uid
            }

            self.alumno_repo.create(alumno)
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