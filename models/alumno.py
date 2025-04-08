from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from usuario import Usuario

class Alumno(Usuario):
    __tablename__ = "alumnos"

    id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    last_login = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    # Relación con Pregunta y Evaluacion
    preguntas = relationship("Pregunta", back_populates="alumno", cascade="all, delete-orphan")
    evaluaciones = relationship("Evaluacion", back_populates="alumno", cascade="all, delete-orphan")
    asistentes = relationship("Asistente", back_populates="alumnos")

    # Relación con Thread
    threads = relationship("Thread", back_populates="alumno", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Alumno(id={self.id}, email='{self.email}')>"