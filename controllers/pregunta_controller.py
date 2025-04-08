from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.pregunta_schema import PreguntaOut, PreguntaCreate, PreguntaUpdate
from services.pregunta_service import PreguntaService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/preguntas",
    tags=["Preguntas"]
)

@router.get("/", response_model=List[PreguntaOut])
def read_preguntas(db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = PreguntaService(db)
    return service.get_all_preguntas()

@router.get("/{pregunta_id}", response_model=PreguntaOut)
def read_pregunta(pregunta_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = PreguntaService(db)
    try:
        pregunta = service.get_pregunta_by_id(pregunta_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return pregunta

@router.post("/", response_model=PreguntaOut, status_code=201)
def create_pregunta(pregunta: PreguntaCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = PreguntaService(db)
    nuevo_pregunta = service.create_pregunta(pregunta.model_dump())
    return nuevo_pregunta

@router.put("/{pregunta_id}", response_model=PreguntaOut)
def update_pregunta(pregunta_id: int, pregunta_data: PreguntaUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = PreguntaService(db)
    try:
        pregunta_actualizado = service.update_pregunta(pregunta_id, pregunta_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return pregunta_actualizado

@router.delete("/{pregunta_id}", status_code=204)
def delete_pregunta(pregunta_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = PreguntaService(db)
    try:
        service.delete_pregunta(pregunta_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
