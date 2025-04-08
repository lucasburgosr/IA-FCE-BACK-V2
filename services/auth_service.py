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

    async def registrar_alumnos(self, email: str, contrasena: str, dni: str) -> dict:
        endpoint_verificacion = "http://dashboard.fce.uncu.edu.ar:5000/alutivos/verificaralumnotutor"
        payload = {"documento": dni}
        
        async with httpx.AsyncClient() as client:
            response = await client.post(
                endpoint_verificacion, 
                json=payload,
                headers={"Content-Type": "application/json"}
            )
        
        if response.status_code != 200:
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
        if alumno_info.get("claustro") != "EST" or alumno_info.get("calidad") != "A":
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El alumno no cumple con los criterios de verificación"
            )
        
        try:
            firebase_user = await asyncio.to_thread(auth.create_user, email=email, password=contrasena)
            firebase_uid = firebase_user.uid
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al crear usuario en Firebase: {str(e)}"
            )
        
        try:
            existing_user = self.alumno_repo.get_by_email(email)
            if existing_user:
                raise HTTPException(
                    status_code=status.HTTP_409_CONFLICT,
                    detail="El usuario ya está registrado"
                )
            nuevo_alumno = Alumno(
                email=email,
                contrasena=contrasena,
                firebase_uid=firebase_uid
            )

            nuevo_alumno.nombres = alumno_info.get("nombres")
            nuevo_alumno.apellido = alumno_info.get("apellido")
            nuevo_alumno.nro_documento = alumno_info.get("nro_documento")
            
            self.alumno_repo.create(nuevo_alumno)
            self.db.commit()
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Error al registrar el usuario en la base de datos: {str(e)}"
            )
        
        return {
            "message": "Usuario registrado exitosamente",
            "firebase_uid": firebase_uid,
            "email": email
        }