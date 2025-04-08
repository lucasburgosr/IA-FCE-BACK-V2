from config.db_config import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Materia(Base):
    __tablename__ = "materias"

    materia_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False, unique=True)

    # Relación con Unidad: una materia contiene varias unidades
    unidades = relationship("Unidad", back_populates="materia", cascade="all, delete-orphan")
    profesores = relationship("Profesor", back_populates="materias")

    def __repr__(self):
        return f"<Materia(materia_id={self.materia_id}, nombre='{self.nombre}')>"