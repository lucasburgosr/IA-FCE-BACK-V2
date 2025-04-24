# controllers/session_controller.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from models.sesion_chat import SesionChat
from config.db_config import get_db
from datetime import datetime, timezone
from utils.dependencies import get_current_user

router = APIRouter(prefix="/sesiones", tags=["Sessions"])

@router.post("/iniciar", response_model=int)
def start_session(thread_id: str, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    alumno_id = current_user["uid_alumno"]  # extraes el id de la sesión decoded_token
    session = SesionChat(alumno_id=alumno_id, thread_id=thread_id)
    db.add(session)
    db.commit()
    db.refresh(session)
    return session.sesion_id

@router.post("/terminar", response_model=None)
def end_session(session_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    sess = db.query(SesionChat).filter_by(session_id=session_id).one_or_none()
    if not sess or sess.finalizada_en:
        raise HTTPException(404, "Sesión no encontrada o ya finalizada")
    sess.finalizada_en = datetime.now(timezone.utc)
    delta = sess.finalizada_en - sess.iniciada_en
    sess.alumno.tiempo_interracion += delta
    db.commit()
    return
