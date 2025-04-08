from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.unidad_schema import UnidadOut, UnidadCreate, UnidadUpdate
from services.unidad_service import UnidadService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/unidades",
    tags=["Unidades"]
)

@router.get("/", response_model=List[UnidadOut])
def read_unidades(db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = UnidadService(db)
    return service.get_all_unidades()

@router.get("/{unidad_id}", response_model=UnidadOut)
def read_unidad(unidad_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = UnidadService(db)
    try:
        unidad = service.get_unidad_by_id(unidad_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return unidad

@router.post("/", response_model=UnidadOut, status_code=201)
def create_unidad(unidad: UnidadCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = UnidadService(db)
    nuevo_unidad = service.create_unidad(unidad.model_dump())
    return nuevo_unidad

@router.put("/{unidad_id}", response_model=UnidadOut)
def update_unidad(unidad_id: int, unidad_data: UnidadUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = UnidadService(db)
    try:
        unidad_actualizado = service.update_unidad(unidad_id, unidad_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return unidad_actualizado

@router.delete("/{unidad_id}", status_code=204)
def delete_unidad(unidad_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = UnidadService(db)
    try:
        service.delete_unidad(unidad_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
