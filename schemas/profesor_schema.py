from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

# schemas/profesor_schema.py

from pydantic import BaseModel, EmailStr
from typing import Optional

# Schema base: define los campos comunes para Profesor
class ProfesorBase(BaseModel):
    email: EmailStr
    materia: str
    firebase_uid: Optional[str] = None
    contrasena: str

# Schema para crear un Profesor
class ProfesorCreate(ProfesorBase):
    pass

# Schema para actualizar un Profesor (actualización parcial)
class ProfesorUpdate(BaseModel):
    email: Optional[EmailStr] = None
    contrasena: Optional[str] = None
    materia: Optional[str] = None

# Schema para la respuesta (output)
class ProfesorOut(ProfesorBase):
    profesor_id: int

    class Config:
        orm_mode = True