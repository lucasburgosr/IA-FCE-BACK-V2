from config.db_config import Base
from sqlalchemy import Column, Integer, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone

class Pregunta(Base):
    __tablename__ = "pregunta"

    pregunta_id = Column(Integer, primary_key=True, index=True)
    contenido = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    subtema_id = Column(Integer, ForeignKey("subtema.subtema_id"), nullable=False)
    unidad_id = Column(Integer, ForeignKey("unidad.unidad_id"), nullable=False)
    alumno_id = Column(Integer, ForeignKey("alumno.alumno_id"), nullable=False)

    def __repr__(self):
        return f"<Pregunta(pregunta_id={self.pregunta_id}, contenido='{self.contenido[:20]}...')>"