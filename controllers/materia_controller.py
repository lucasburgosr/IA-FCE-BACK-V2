from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.materia_schema import MateriaOut, MateriaCreate, MateriaUpdate
from services.materia_service import MateriaService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/materias",
    tags=["Materias"]
)

@router.get("/", response_model=List[MateriaOut])
def read_materias(db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = MateriaService(db)
    return service.get_all_materias()

@router.get("/{materia_id}", response_model=MateriaOut)
def read_materia(materia_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = MateriaService(db)
    try:
        materia = service.get_materia_by_id(materia_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return materia

@router.post("/", response_model=MateriaOut, status_code=201)
def create_materia(materia: MateriaCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = MateriaService(db)
    nuevo_materia = service.create_materia(materia.model_dump())
    return nuevo_materia

@router.put("/{materia_id}", response_model=MateriaOut)
def update_materia(materia_id: int, materia_data: MateriaUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = MateriaService(db)
    try:
        materia_actualizado = service.update_materia(materia_id, materia_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return materia_actualizado

@router.delete("/{materia_id}", status_code=204)
def delete_materia(materia_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = MateriaService(db)
    try:
        service.delete_materia(materia_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
