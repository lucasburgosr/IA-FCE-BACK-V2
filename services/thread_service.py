import asyncio
from repositories.thread_repository import ThreadRepository
from typing import Dict, Any, List
from models.thread import Thread
from sqlalchemy.orm import Session
from openai import OpenAI
from datetime import datetime
from schemas.mensaje_schema import MensajeOut
from repositories.asistente_repository import AsistenteRepository
from services.asistente_service import AsistenteService
from services.alumno_service import AlumnoService

client = OpenAI()


class ThreadService:
    def __init__(self, db: Session):
        self.db = db
        self.thread_repo = ThreadRepository(db)
        self.asistente_repo = AsistenteRepository(db)

    async def get_thread_by_id(self, id: str) -> Thread:
        thread = self.thread_repo.get_by_id(id)
        if not thread:
            raise ValueError(f"Thread con id {id} no encontrado")
        return thread
    
    async def get_thread_by_alumno(self, alumno_id: int) -> Thread:
        thread = self.thread_repo.get_by_alumno(alumno_id=alumno_id)
        if not thread:
            return self.create_thread(alumno_id=alumno_id)
        
        return thread

    async def get_all_threads(self) -> List[Thread]:
        return self.thread_repo.get_all()

    # Método que crea un thread en la API de OpenAI y en nuestra DB relacionándolo con un asistente y un estudiante
    def create_thread(self, thread_data: dict) -> Thread:
        alumno_id = thread_data["alumnoId"]
        asistente_id = thread_data["asistente_id"]

        thread = client.beta.threads.create()
        thread_db = self.thread_repo.create({
            "id": thread.id,
            "alumno_id": alumno_id
        })

        asistente = self.asistente_repo.get_by_id(asistente_id=asistente_id)

        if not asistente:
            raise ValueError("No se encontró el asistente")
        
        thread_db.asistentes.append(asistente)

        self.db.commit()
        self.db.refresh(thread_db)

        return thread

    async def update_thread(self, id: str, update_data: Dict[str, Any]) -> Thread:
        thread = self.thread_repo.get_by_id(id)
        return self.thread_repo.update(thread, update_data)

    async def delete_thread(self, id: str) -> None:
        thread = self.thread_repo.get_by_id(id)
        self.thread_repo.delete(thread)

    # Obtenemos la lista de mensajes de OpenAI y los ordenamos por timestamp para mostrarlos en el chat
    async def get_messages(self, id: str) -> List[MensajeOut]:
        response = await asyncio.to_thread(client.beta.threads.messages.list, thread_id=id)
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

    # Método que recibe los ID de thread y asistente y el texto enviado por el usuario para generar una respuesta con un 
    # modelo de OpenAI
    # También incrementamos el contador de mensajes enviados por el alumno con increment_message_count()
    async def send_message(self, id: str, texto: str, asistente_id: str, alumno_id: int) -> Dict[str, Any]:
        try:
            mensaje = await asyncio.to_thread(client.beta.threads.messages.create,
                                    thread_id=id,
                                    content=texto,
                                    role="user")
            alumno_service = AlumnoService(self.db)
            alumno_service.increment_message_count(alumno_id=alumno_id)
            # Para acceder al mensaje generado por el Asistente hay que traer de nuevo la lista
            # de mensajes, acá solo devolvemos el estado del objeto run
            run = await asyncio.to_thread(client.beta.threads.runs.create_and_poll,
                                thread_id=id,
                                assistant_id=asistente_id)
            
            return run.status
        except Exception as e:
            return {"error": str(e)}
        
    # REVISAR EL USO DE ESTE MÉTODO
    """ async def join_thread_asistente(self, id: str, asistente_id: str):
        thread = self.get_thread_by_id(id=id)
        asistente_service = AsistenteService(db=self.db)
        asistente = asistente_service.get_asistente_by_id(asistente_id=asistente_id)

        if not thread or not asistente:
            raise ValueError("Thread o Asistente no encontrados")
        
        thread.asistentes.append(asistente)
        self.db.commit() """
