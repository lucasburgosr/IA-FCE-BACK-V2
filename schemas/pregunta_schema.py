# schemas/pregunta_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema base: define los campos esenciales de una pregunta
class PreguntaBase(BaseModel):
    contenido: str
    subtema_id: int
    id: int

# Schema para la creación de una pregunta (input)
class PreguntaCreate(PreguntaBase):
    pass

# Schema para la actualización de una pregunta (input parcial)
class PreguntaUpdate(BaseModel):
    contenido: Optional[str] = None
    subtema_id: Optional[int] = None
    id: Optional[int] = None

# Schema de salida (output): incluye identificador y fecha de creación
class PreguntaOut(PreguntaBase):
    pregunta_id: int
    created_at: datetime

    class Config:
        orm_mode = True
