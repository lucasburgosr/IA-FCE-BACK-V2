from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.evaluacion_schema import EvaluacionOut, EvaluacionCreate, EvaluacionUpdate
from services.evaluacion_service import EvaluacionService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/evaluaciones",
    tags=["Evaluaciones"]
)

@router.get("/", response_model=List[EvaluacionOut])
def read_evaluaciones(db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = EvaluacionService(db)
    return service.get_all_evaluaciones()

@router.get("/{evaluacion_id}", response_model=EvaluacionOut)
def read_evaluacion(evaluacion_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = EvaluacionService(db)
    try:
        evaluacion = service.get_evaluacion_by_id(evaluacion_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return evaluacion

@router.post("/", response_model=EvaluacionOut, status_code=201)
def create_evaluacion(evaluacion: EvaluacionCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = EvaluacionService(db)
    nuevo_evaluacion = service.create_evaluacion(evaluacion.model_dump())
    return nuevo_evaluacion

@router.put("/{evaluacion_id}", response_model=EvaluacionOut)
def update_evaluacion(evaluacion_id: int, evaluacion_data: EvaluacionUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = EvaluacionService(db)
    try:
        evaluacion_actualizado = service.update_evaluacion(evaluacion_id, evaluacion_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return evaluacion_actualizado

@router.delete("/{evaluacion_id}", status_code=204)
def delete_evaluacion(evaluacion_id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = EvaluacionService(db)
    try:
        service.delete_evaluacion(evaluacion_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
