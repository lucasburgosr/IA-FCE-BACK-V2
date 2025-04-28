from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from schemas.materia_schema import MateriaOut, MateriaBase
from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema base: define los campos comunes para Profesor
class ProfesorBase(BaseModel):
    email: EmailStr
    materia: MateriaOut
    firebase_uid: Optional[str] = None
    contrasena: str

# Schema para crear un Profesor
class ProfesorCreate(ProfesorBase):
    pass

# Schema para actualizar un Profesor (actualización parcial)
class ProfesorUpdate(BaseModel):
    email: Optional[EmailStr] = None
    contrasena: Optional[str] = None
    materia_id: int = None

# Schema para la respuesta (output)
class ProfesorOut(BaseModel):
    profesor_id: int
    email: EmailStr
    materia: MateriaOut
    firebase_uid: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True