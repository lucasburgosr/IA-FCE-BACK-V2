# schemas/materia_schema.py

from pydantic import BaseModel
from typing import List, Optional

from schemas.unidad_schema import UnidadOut

# Schema base: define los campos comunes para Materia
class MateriaBase(BaseModel):
    nombre: str

# Schema para la creación de una Materia
class MateriaCreate(MateriaBase):
    pass

# Schema para la actualización de una Materia (actualización parcial)
class MateriaUpdate(BaseModel):
    nombre: Optional[str] = None

# Schema de salida (output) para Materia
class MateriaOut(MateriaBase):
    materia_id: int
    unidades: List[UnidadOut] = []

    class Config:
        orm_mode = True
