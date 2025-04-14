# schemas/asistente_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema base: define los campos comunes para Asistente
class AsistenteBase(BaseModel):
    nombre: str
    instructions: str

# Schema para la creación de un Asistente
class AsistenteCreate(AsistenteBase):
    pass

# Schema para la actualización (todos los campos son opcionales)
class AsistenteUpdate(BaseModel):
    nombre: Optional[str] = None
    instructions: Optional[str] = None

# Schema de salida (output), incluye el id y los campos de fecha
class AsistenteOut(AsistenteBase):
    asistente_id: str

    class Config:
        orm_mode = True
