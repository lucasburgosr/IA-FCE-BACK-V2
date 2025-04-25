# services/session_service.py
from typing import Optional
from sqlalchemy.orm import Session
from models.sesion_chat import SesionChat
from repositories.sesion_chat_repository import SessionRepository

class SesionService:
    def __init__(self, db: Session):
        self.repo = SessionRepository(db)

    def start_session(self, alumno_id: int, thread_id: str) -> SesionChat:
        return self.repo.create(alumno_id, thread_id)

    def end_session(self, sesion_id: int) -> None:
        session = self.repo.finish(sesion_id)
        if session is None:
            raise ValueError(f"Sesión {sesion_id} no encontrada o ya finalizada")
