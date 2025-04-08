from config.db_config import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Pregunta(Base):
    __tablename__ = "preguntas"

    pregunta_id = Column(Integer, primary_key=True, index=True)
    contenido = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    # Claves foráneas: Subtema y Alumno
    subtema_id = Column(Integer, ForeignKey("subtemas.subtema_id"), nullable=False)
    id = Column(Integer, ForeignKey("alumnos.id"), nullable=False)

    subtema = relationship("Subtema", back_populates="preguntas")
    alumno = relationship("Alumno", back_populates="preguntas")

    def __repr__(self):
        return f"<Pregunta(pregunta_id={self.pregunta_id}, contenido='{self.contenido[:20]}...')>"