# services/session_service.py
from typing import Optional
from openai import OpenAI
from datetime import datetime
from sqlalchemy.orm import Session
from models.sesion_chat import SesionChat
from repositories.sesion_chat_repository import SessionRepository
from repositories.alumno_repository import AlumnoRepository

client = OpenAI()


class SesionService:
    def __init__(self, db: Session):
        self.repo = SessionRepository(db)
        self.alumno_repo = AlumnoRepository(db)

    def start_session(self, alumno_id: int, thread_id: str) -> SesionChat:
        return self.repo.create(alumno_id, thread_id)

    def end_session(self, sesion_id: int, thread_id: str, alumno_id: int) -> None:
        service = SesionService(self.repo.db)
        session = self.repo.finish(sesion_id)
        sesion_resumen = self.repo.get_by_id(sesion_id=sesion_id)
        service.resumir_ultima_conversacion(
            alumno_id=alumno_id, filtro_fecha=sesion_resumen.iniciada_en, thread_id=thread_id)

        if session is None:
            raise ValueError(
                f"Sesión {sesion_id} no encontrada o ya finalizada")

    def resumir_ultima_conversacion(self, alumno_id: int, filtro_fecha: datetime, thread_id: str):
        mensajes = client.beta.threads.messages.list(thread_id=thread_id)

        filtro = int(filtro_fecha.timestamp())

        print(filtro)

        mensajes_filtrados = [
            m for m in mensajes.data if m.created_at >= filtro
        ]

        print(mensajes_filtrados)

        mensajes_formatted = []


        for m in mensajes_filtrados:
            if m.role not in {"user", "assistant"}:
                continue

            for content_block in m.content:
                if content_block.type == "text" and hasattr(content_block, "text"):
                    texto = getattr(content_block.text, "value", "").strip()
                    if texto:
                        mensajes_formatted.append({
                            "role": m.role,
                            "content": texto
                        })

        for m in mensajes_formatted:
            print(m)

        resumen_prompt = [
            {
                "role": "system",
                "content": "Eres un asistente que ayuda a resumir conversaciones entre un estudiante de Matemática de nivel universitario y un tutor virtual. Escribe un resumen breve (3 a 5 líneas) de lo que se discutió en esta sesión sin importar la brevedad o extensión de la misma."
            },
            *mensajes_formatted,
            {
                "role": "user",
                "content": "¿Podrías escribir un resumen de esta sesión?"
            }
        ]

        response = client.chat.completions.create(
            model="gpt-4",
            messages=resumen_prompt,
        )

        resumen = response.choices[0].message.content

        update_data = {
            "resumen_ultima_sesion": resumen
        }
        print(resumen)
        alumno = self.alumno_repo.get_by_id(id=alumno_id)
        self.alumno_repo.update(alumno=alumno, update_data=update_data)
