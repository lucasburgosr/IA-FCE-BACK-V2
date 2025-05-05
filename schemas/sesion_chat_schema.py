# schemas/session_schema.py
from pydantic import BaseModel

class SesionStartRequest(BaseModel):
    thread_id: str

class SesionStartResponse(BaseModel):
    sesion_id: int

class SesionEndRequest(BaseModel):
    alumno_id: int
    sesion_id: int
    thread_id: str
