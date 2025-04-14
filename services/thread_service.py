import asyncio
from pydantic import BaseModel, field_validator
from repositories.thread_repository import ThreadRepository
from config.db_config import Base
from typing import Dict, Any, List
from models.thread import Thread
from sqlalchemy.orm import Session
from openai import OpenAI
from datetime import datetime
from schemas.mensaje_schema import MensajeOut, MensajeCreate

client = OpenAI()


class ThreadService:
    def __init__(self, db: Session):
        self.db = db
        self.thread_repo = ThreadRepository(db)

    def get_thread_by_id(self, thread_id: str) -> Thread:
        thread = self.thread_repo.get_by_id(thread_id)
        if not thread:
            raise ValueError(f"Thread con id {thread_id} no encontrado")
        return thread

    def get_all_threads(self) -> List[Thread]:
        return self.thread_repo.get_all()

    def create_thread(self) -> Thread:
        thread = client.beta.threads.create()
        thread_db = self.thread_repo.create()
        thread_db.thread_id = thread.id
        return thread

    def update_thread(self, thread_id: str, update_data: Dict[str, Any]) -> Thread:
        thread = self.thread_repo.get_by_id(thread_id)
        return self.thread_repo.update(thread, update_data)

    def delete_thread(self, thread_id: str) -> None:
        thread = self.thread_repo.get_by_id(thread_id)
        self.thread_repo.delete(thread)

    async def get_messages(self, thread_id: str) -> List[MensajeOut]:
        response = await asyncio.to_thread(client.beta.threads.messages.list, thread_id=thread_id)
        mensajes = [
            MensajeOut(
                id=mensaje.id,
                texto=mensaje.content[0].text.value,
                rol=mensaje.role,
                fecha=mensaje.created_at
            ) for mensaje in response.data
        ]
        mensajes.sort(key=lambda x: x.fecha)
        return mensajes

    async def send_message(self, thread_id: str, texto: str, asistente_id: str) -> Dict[str, Any]:
        try:
            mensaje = await asyncio(client.beta.threads.messages.create,
                                    thread_id=thread_id,
                                    content=texto,
                                    role="user")
            # Para acceder al mensaje generado por el Asistente hay que traer de nuevo la lista
            # de mensajes
            run = await asyncio(client.beta.threads.runs.create_and_poll,
                                thread_id=thread_id,
                                assistant_id=asistente_id)
            
            return run.status
        except Exception as e:
            return {"error": str(e)}
