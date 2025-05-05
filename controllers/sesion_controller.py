# controllers/session_controller.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from config.db_config import get_db
from utils.dependencies import get_current_user
from schemas.sesion_chat_schema import (
    SesionStartRequest,
    SesionStartResponse,
    SesionEndRequest
)
from services.sesion_chat_service import SesionService

router = APIRouter(prefix="/sesiones", tags=["Sesiones"])


@router.post("/iniciar/{alumno_id}", response_model=SesionStartResponse, status_code=status.HTTP_201_CREATED)
async def start_session(alumno_id: int, req: SesionStartRequest, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    print(alumno_id)
    service = SesionService(db)
    session = service.start_session(alumno_id, req.thread_id)
    return SesionStartResponse(sesion_id=session.sesion_id)


@router.post(
    "/finalizar",
    status_code=status.HTTP_204_NO_CONTENT
)
async def end_session(
    req: SesionEndRequest,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = SesionService(db)
    try:
        print("THREAD ID:", req.thread_id)
        print("ALUMNO ID:", req.alumno_id)
        print("SESION ID:", req.sesion_id)
        service.end_session(alumno_id=req.alumno_id, thread_id=req.thread_id, sesion_id=req.sesion_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return