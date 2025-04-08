# schemas/evaluacion_schema.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Schema base: define los campos comunes a Evaluación
class EvaluacionBase(BaseModel):
    nota: float
    subtema_id: int
    id: int

# Schema para la creación de una Evaluación (input)
class EvaluacionCreate(EvaluacionBase):
    pass

# Schema para actualización (input parcial)
class EvaluacionUpdate(BaseModel):
    nota: Optional[float] = None
    subtema_id: Optional[int] = None
    id: Optional[int] = None

# Schema de salida (output): incluye identificador y fecha de evaluación
class EvaluacionOut(EvaluacionBase):
    evaluacion_id: int
    evaluacion_fecha: datetime

    class Config:
        orm_mode = True
