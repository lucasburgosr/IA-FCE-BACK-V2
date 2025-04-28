from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class AsistenteBase(BaseModel):
    nombre: str = Field(..., alias="name")   # <--- ALIAS!!
    instructions: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True  # permite usar "nombre" internamente y "name" externamente

class AsistenteCreate(AsistenteBase):
    pass

class AsistenteUpdate(BaseModel):
    nombre: Optional[str] = Field(None, alias="name")
    instructions: Optional[str] = None

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class AsistenteDBOut(AsistenteBase):
    asistente_id: str
    nombre: str

class AsistenteOpenAIOut(AsistenteBase):
    asistente_id: str
    name: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
