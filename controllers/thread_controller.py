from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional, Any, Dict
from schemas.thread_schema import ThreadOut, ThreadCreate, ThreadUpdate
from services.thread_service import ThreadService
from schemas.mensaje_schema import MensajeOut
from config.db_config import get_db
from utils.dependencies import get_current_user

router = APIRouter(
    prefix="/threads",
    tags=["Threads"]
)

@router.get("/", response_model=List[ThreadOut])
async def read_threads(db: Session = Depends(get_db),
                 current_user: dict = Depends(get_current_user)):
    service = ThreadService(db)
    return await service.get_all_threads()


@router.get("/{thread_id}", response_model=ThreadOut)
async def read_thread(thread_id: str, db: Session = Depends(get_db),
                current_user: dict = Depends(get_current_user)):
    service = ThreadService(db)
    try:
        thread = await service.get_thread_by_id(thread_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return thread

@router.get("/{alumno_id}", response_model=ThreadOut)
async def read_thread_by_alumno(alumno_id: int, db: Session = Depends(get_db),
                current_user: dict = Depends(get_current_user)):
    service = ThreadService(db)
    try:
        thread = await service.get_thread_by_alumno(alumno_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return thread


@router.post("/", response_model=ThreadOut, status_code=201)
def create_thread(thread: dict, db: Session = Depends(get_db),
                  current_user: dict = Depends(get_current_user)):
    service = ThreadService(db)
    nuevo_thread = service.create_thread(thread)
    return nuevo_thread

# Poco probable que sea utilizado
""" @router.put("/{thread_id}", response_model=ThreadOut)
async def update_thread(thread_id: str, thread_data: ThreadUpdate, db: Session = Depends(get_db),
                  current_user: dict = Depends(get_current_user)):
    service = ThreadService(db)
    try:
        thread_actualizado = await service.update_thread(
            thread_id, thread_data.model_dump(exclude_unset=True))
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return thread_actualizado """


@router.delete("/{thread_id}", status_code=204)
async def delete_thread(thread_id: str, db: Session = Depends(get_db),
                  current_user: dict = Depends(get_current_user)):
    service = ThreadService(db)
    try:
        await service.delete_thread(thread_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    return


@router.get("/{thread_id}/messages", response_model=List[MensajeOut])
async def read_thread_messages(thread_id: str, db: Session = Depends(get_db)):
    service = ThreadService(db)
    try:
        mensajes = await service.get_messages(thread_id=thread_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
    return mensajes


@router.post("/{thread_id}")
async def send_message(mensaje_data: dict, db: Session = Depends(get_db), current_user: dict = Depends(get_current_user)):
    try:

        texto = mensaje_data["input"]
        thread_id = mensaje_data["thread_id"]
        asistente_id = mensaje_data["asistente_id"]

        service = ThreadService(db)
        response = await service.send_message(thread_id=thread_id, texto=texto, asistente_id=asistente_id)

        if response == "completed":
            mensajes = await service.get_messages(thread_id=thread_id)
            return mensajes

    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
