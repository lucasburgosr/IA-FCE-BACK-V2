from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.alumno_schema import AlumnoOut, AlumnoCreate, AlumnoUpdate
from services.alumno_service import AlumnoService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/alumnos",
    tags=["Alumnos"]
)

@router.get("/", response_model=List[AlumnoOut])
def read_alumnos(
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    service = AlumnoService(db)
    return service.get_all_alumnos()

@router.get("/{id}", response_model=AlumnoOut)
def read_alumno(id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AlumnoService(db)
    try:
        alumno = service.get_alumno_by_id(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return alumno

@router.get("by-email", response_model=AlumnoOut)
def read_alumno_by_email(email: str, db: Session = Depends(get_db)):

    service = AlumnoService(db)
    try:
        alumno = service.get_alumno_by_email(email)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return alumno

@router.post("/", response_model=AlumnoOut, status_code=201)
def create_alumno(alumno: AlumnoCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AlumnoService(db)
    nuevo_alumno = service.create_alumno(alumno.model_dump())
    return nuevo_alumno

@router.put("/{id}", response_model=AlumnoOut)
def update_alumno(id: int, alumno_data: AlumnoUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AlumnoService(db)
    try:
        alumno_actualizado = service.update_alumno(id, alumno_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return alumno_actualizado

@router.delete("/{id}", status_code=204)
def delete_alumno(id: int, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AlumnoService(db)
    try:
        service.delete_alumno(id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
