# schemas/thread_schema.py

from pydantic import BaseModel
from datetime import datetime
from typing import Optional

# Schema base: define los campos esenciales para un Thread
class ThreadBase(BaseModel):
    title: Optional[str] = None
    id: int

# Schema para la creación de un Thread (input)
class ThreadCreate(ThreadBase):
    pass

# Schema para actualizar un Thread (input parcial)
class ThreadUpdate(BaseModel):
    title: Optional[str] = None
    id: Optional[int] = None

# Schema de salida (output) para Thread
class ThreadOut(ThreadBase):
    thread_id: str
    started_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
