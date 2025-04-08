from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.subtema_schema import SubtemaOut, SubtemaCreate, SubtemaUpdate
from services.subtema_service import SubtemaService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/subtemas",
    tags=["Subtemas"]
)

@router.get("/", response_model=List[SubtemaOut])
def read_subtemas(db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = SubtemaService(db)
    return service.get_all_subtemas()

@router.get("/{subtema_id}", response_model=SubtemaOut)
def read_subtema(subtema_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = SubtemaService(db)
    try:
        subtema = service.get_subtema_by_id(subtema_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return subtema

@router.post("/", response_model=SubtemaOut, status_code=201)
def create_subtema(subtema: SubtemaCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = SubtemaService(db)
    nuevo_subtema = service.create_subtema(subtema.model_dump())
    return nuevo_subtema

@router.put("/{subtema_id}", response_model=SubtemaOut)
def update_subtema(subtema_id: int, subtema_data: SubtemaUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = SubtemaService(db)
    try:
        subtema_actualizado = service.update_subtema(subtema_id, subtema_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return subtema_actualizado

@router.delete("/{subtema_id}", status_code=204)
def delete_subtema(subtema_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = SubtemaService(db)
    try:
        service.delete_subtema(subtema_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
