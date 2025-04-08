from pydantic import BaseModel, field_validator
from datetime import datetime


class MensajeBase(BaseModel):
    texto: str
    rol: str

class MensajeCreate(MensajeBase):
    thread_id: str

class MensajeOut(MensajeBase):
    id: str
    fecha: datetime

    @field_validator("fecha", mode="before")
    def convertir_timestamp(cls, value):
        if isinstance(value, int):
            return datetime.fromtimestamp(value)
        return value