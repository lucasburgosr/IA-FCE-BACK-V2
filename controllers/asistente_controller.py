from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from schemas.asistente_schema import AsistenteDBOut, AsistenteCreate, AsistenteUpdate, AsistenteOpenAIOut
from services.asistente_service import AsistenteService
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/asistentes",
    tags=["Asistentes"]
)

@router.get("/", response_model=List[AsistenteDBOut])
def read_asistentes(db: Session = Depends(get_db)):
    service = AsistenteService(db)
    return service.get_all_asistentes()

# Obtiene el asistente de la API y lo mapeamos a un diccionario con el nombre de las propiedades que necesitamos en el cliente
@router.get("/{asistente_id}", response_model=AsistenteOpenAIOut)
def read_asistente(asistente_id: str, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AsistenteService(db)
    try:
        asistente_openai = service.get_asistente_by_id(asistente_id)
        asistente_dict = {
            "asistente_id": asistente_openai.id,
            "name": asistente_openai.name,
            "instructions": asistente_openai.instructions,
        }
        return AsistenteOpenAIOut.model_validate(asistente_dict)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


""" @router.post("/", response_model=AsistenteDBOut, status_code=201)
def create_asistente(asistente: AsistenteCreate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AsistenteService(db)
    nuevo_asistente = service.create_asistente(asistente.model_dump())
    return nuevo_asistente """

# Llamamos al método que actualiza ambos Asistentes.
@router.put("/{asistente_id}", response_model=AsistenteOpenAIOut)
def update_asistente(asistente_id: str, asistente_data: AsistenteUpdate, db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)):
    service = AsistenteService(db)
    try:
        asistente_actualizado = service.update_asistente(asistente_id, asistente_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return AsistenteOpenAIOut.model_validate(asistente_actualizado)

@router.delete("/{asistente_id}", status_code=204)
def delete_asistente(asistente_id: str, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    service = AsistenteService(db)
    try:
        service.delete_asistente(asistente_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return
