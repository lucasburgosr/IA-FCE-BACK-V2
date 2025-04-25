# repositories/session_repository.py
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy.orm import Session
from models.sesion_chat import SesionChat

class SessionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, alumno_id: int, thread_id: str) -> SesionChat:
        session = SesionChat(
            alumno_id=alumno_id,
            thread_id=thread_id,
            iniciada_en=datetime.now(timezone.utc)
        )
        self.db.add(session)
        self.db.commit()
        self.db.refresh(session)
        return session

    def finish(self, sesion_id: int) -> Optional[SesionChat]:
        session = (
            self.db
            .query(SesionChat)
            .filter_by(sesion_id=sesion_id)
            .one_or_none()
        )
        if not session or session.finalizada_en is not None:
            return None

        session.finalizada_en = datetime.now(timezone.utc)
        # Actualizo el tiempo_interaccion en alumno
        delta = session.finalizada_en - session.iniciada_en
        session.alumno.tiempo_interaccion += delta

        self.db.commit()
        self.db.refresh(session)
        return session
