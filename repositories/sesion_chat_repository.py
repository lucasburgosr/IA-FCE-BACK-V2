from sqlalchemy.orm import Session
from models.sesion_chat import SesionChat
from datetime import datetime, timedelta, timezone

class SessionRepository:
    def __init__(self, db: Session):
        self.db = db

    def start(self, alumno_id: int, thread_id: str) -> SesionChat:
        s = SesionChat(alumno_id=alumno_id, thread_id=thread_id)
        self.db.add(s); self.db.commit(); self.db.refresh(s)
        return s

    def end(self, session_id: int) -> timedelta:
        s = self.db.query(SesionChat).get(session_id)
        if not s or s.finalizada_en:
            return None
        s.ended_at = datetime.now(timezone.utc)
        delta = s.finalizada_en - s.iniciada_en
        s.alumno.tiempo_interaccion += delta
        self.db.commit()
        return delta
