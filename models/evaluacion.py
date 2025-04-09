from config.db_config import Base
from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Evaluacion(Base):
    __tablename__ = "evaluacion"

    evaluacion_id = Column(Integer, primary_key=True, index=True)
    nota = Column(Float, nullable=False)
    evaluacion_fecha = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    # Claves foráneas: Subtema y Alumno
    subtema_id = Column(Integer, ForeignKey("subtema.subtema_id"), nullable=False)
    alumno_id = Column(Integer, ForeignKey("alumno.alumno_id"), nullable=False)

    def __repr__(self):
        return f"<Evaluacion(evaluacion_id={self.evaluacion_id}, nota={self.nota})>"