from config.db_config import Base
from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship

class Subtema(Base):
    __tablename__ = "subtema"

    subtema_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    unidad_id = Column(Integer, ForeignKey("unidad.unidad_id"), nullable=False)

    preguntas = relationship("Pregunta", backref="subtema", cascade="all, delete-orphan")
    evaluaciones = relationship("Evaluacion", backref="subtema", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Subtema(subtema_id={self.subtema_id}, nombre='{self.nombre}')>"