# schemas/materia_schema.py

from pydantic import BaseModel
from typing import List, Optional
from schemas.asistente_schema import AsistenteDBOut
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
    asistente: Optional[AsistenteDBOut] = None   # <--- este agregado es necesario

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
