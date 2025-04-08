from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.profesor_schema import ProfesorOut, ProfesorCreate, ProfesorUpdate
from services.profesor_service import ProfesorService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/profesores",
    tags=["Profesores"]
)

@router.get("/", response_model=List[ProfesorOut])
def read_profesores(db: Session = Depends(get_db)):
    service = ProfesorService(db)
    return service.get_all_profesores()

@router.get("/{profesor_id}", response_model=ProfesorOut)
def read_profesor(profesor_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = ProfesorService(db)
    try:
        profesor = service.get_profesor_by_id(profesor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return profesor

@router.post("/", response_model=ProfesorOut, status_code=201)
def create_profesor(profesor: ProfesorCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = ProfesorService(db)
    nuevo_profesor = service.create_profesor(profesor.model_dump())
    return nuevo_profesor

@router.put("/{profesor_id}", response_model=ProfesorOut)
def update_profesor(profesor_id: int, profesor_data: ProfesorUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = ProfesorService(db)
    try:
        profesor_actualizado = service.update_profesor(profesor_id, profesor_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return profesor_actualizado

@router.delete("/{profesor_id}", status_code=204)
def delete_profesor(profesor_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = ProfesorService(db)
    try:
        service.delete_profesor(profesor_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
