from sqlalchemy import Column, Integer, DateTime, ForeignKey, Interval, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone, timedelta
from models.usuario import Usuario
from models.alumno_asistente import alumno_asistente


class Alumno(Usuario):
    __tablename__ = "alumno"

    alumno_id = Column(Integer, ForeignKey("usuario.id"), primary_key=True)
    last_login = Column(DateTime(timezone=True),
                        default=datetime.now(timezone.utc))
    mensajes_enviados = Column(Integer, default=0, nullable=False)
    tiempo_interaccion = Column(
        Interval, default=lambda: timedelta(), nullable=False)
    resumen_ultima_sesion = Column(Text, nullable=True)

    # Relaciones
    preguntas = relationship("Pregunta", backref="alumno",
                             cascade="all, delete-orphan")
    evaluaciones = relationship(
        "Evaluacion", backref="alumno", cascade="all, delete-orphan")
    asistentes = relationship(
        "Asistente", secondary=alumno_asistente, backref="alumno")
    threads = relationship("Thread", backref="alumno",
                           cascade="all, delete-orphan")
    sesiones = relationship(
        "SesionChat",
        back_populates="alumno",
        cascade="all, delete-orphan"
    )

    __mapper_args__ = {
        "polymorphic_identity": "alumno"
    }

    def __repr__(self):
        return f"<Alumno(id={self.alumno_id}, email='{self.email}')>"
