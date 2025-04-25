# schemas/session_schema.py
from pydantic import BaseModel

class SesionStartRequest(BaseModel):
    thread_id: str

class SesionStartResponse(BaseModel):
    sesion_id: int

class SesionEndRequest(BaseModel):
    sesion_id: int
