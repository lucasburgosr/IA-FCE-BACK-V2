from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from config.db_config import Base

class Unidad(Base):
    __tablename__ = "unidad"

    unidad_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    materia_id = Column(Integer, ForeignKey("materia.materia_id"), nullable=False)

    subtemas = relationship("Subtema", backref="unidad", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Unidad(unidad_id={self.unidad_id}, nombre='{self.nombre}')>"