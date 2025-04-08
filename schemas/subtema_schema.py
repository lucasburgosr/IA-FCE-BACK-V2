# schemas/subtema_schema.py

from pydantic import BaseModel
from typing import Optional

# Schema base: define los campos esenciales de un subtema
class SubtemaBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    unidad_id: int

# Schema para la creación de un Subtema
class SubtemaCreate(SubtemaBase):
    pass

# Schema para actualizar un Subtema (actualización parcial)
class SubtemaUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    unidad_id: Optional[int] = None

# Schema de salida (output) para Subtema
class SubtemaOut(SubtemaBase):
    subtema_id: int

    class Config:
        orm_mode = True
