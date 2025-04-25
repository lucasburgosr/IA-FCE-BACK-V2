# schemas/thread_schema.py

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional

# Schema base: define los campos esenciales para un Thread
class ThreadBase(BaseModel):
    title: Optional[str] = None

# Schema para la creación de un Thread (input)
class ThreadCreate(ThreadBase):
    alumno_id: int = Field(..., alias="alumnoId")
    asistente_id: str = Field(..., alias="asistenteId")

# Schema para actualizar un Thread (input parcial)
class ThreadUpdate(BaseModel):
    title: Optional[str] = None
    id: Optional[int] = None

# Schema de salida (output) para Thread
class ThreadOut(ThreadBase):
    id: str

    class Config:
        orm_mode = True
