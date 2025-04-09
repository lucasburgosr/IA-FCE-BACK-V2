from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from models.usuario import Usuario
from models.alumno_asistente import alumno_asistente

class Alumno(Usuario):
    __tablename__ = "alumno"

    alumno_id = Column(Integer, ForeignKey("usuario.id"), primary_key=True)
    last_login = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    # Relación con Pregunta y Evaluacion
    preguntas = relationship("Pregunta", backref="alumno", cascade="all, delete-orphan")
    evaluaciones = relationship("Evaluacion", backref="alumno", cascade="all, delete-orphan")

    asistentes = relationship("Asistente", secondary=alumno_asistente, backref="alumno")

    # Relación con Thread
    threads = relationship("Thread", backref="alumno", cascade="all, delete-orphan")

    __mapper_args__ = {
        "polymorphic_identity": "alumno"
    }

    def __repr__(self):
        return f"<Alumno(id={self.alumno_id}, email='{self.email}')>"