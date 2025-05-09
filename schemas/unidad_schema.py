from pydantic import BaseModel
from typing import List, Optional

from schemas.subtema_schema import SubtemaOut

# Schema base: define los campos comunes de una unidad
class UnidadBase(BaseModel):
    nombre: str
    descripcion: Optional[str] = None
    materia_id: int

# Schema para la creación de una Unidad (input)
class UnidadCreate(UnidadBase):
    pass

# Schema para actualizar una Unidad (actualización parcial)
class UnidadUpdate(BaseModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    materia_id: Optional[int] = None

# Schema de salida (output) para Unidad
class UnidadOut(UnidadBase):
    unidad_id: int
    subtemas: List[SubtemaOut] = []

    class Config:
        orm_mode = True
