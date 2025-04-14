from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.asistente_schema import AsistenteOut, AsistenteCreate, AsistenteUpdate
from services.asistente_service import AsistenteService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/asistentes",
    tags=["Asistentes"]
)

@router.get("/", response_model=List[AsistenteOut])
def read_asistentes(db: Session = Depends(get_db)):
    service = AsistenteService(db)
    return service.get_all_asistentes()

@router.get("/{asistente_id}", response_model=AsistenteOut)
def read_asistente(asistente_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AsistenteService(db)
    try:
        asistente = service.get_asistente_by_id(asistente_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return asistente

@router.post("/", response_model=AsistenteOut, status_code=201)
def create_asistente(asistente: AsistenteCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AsistenteService(db)
    nuevo_asistente = service.create_asistente(asistente.model_dump())
    return nuevo_asistente

@router.put("/{asistente_id}", response_model=AsistenteOut)
def update_asistente(asistente_id: int, asistente_data: AsistenteUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AsistenteService(db)
    try:
        asistente_actualizado = service.update_asistente(asistente_id, asistente_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return asistente_actualizado

@router.delete("/{asistente_id}", status_code=204)
def delete_asistente(asistente_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AsistenteService(db)
    try:
        service.delete_asistente(asistente_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
