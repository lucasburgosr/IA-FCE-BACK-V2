# schemas/asistente_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema base: define los campos comunes para Asistente
class AsistenteBase(BaseModel):
    name: str
    instructions: str

# Schema para la creación de un Asistente
class AsistenteCreate(AsistenteBase):
    pass

# Schema para la actualización (todos los campos son opcionales)
class AsistenteUpdate(BaseModel):
    name: Optional[str] = None
    instructions: Optional[str] = None
    version: Optional[str] = None

# Schema de salida (output), incluye el id y los campos de fecha
class AsistenteOut(AsistenteBase):
    asistente_id: int
    created_at: datetime
    description: str

    class Config:
        orm_mode = True
