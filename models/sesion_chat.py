from config.db_config import Base
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship

class SesionChat(Base):
    __tablename__ = "sesion_chat"

    sesion_id = Column(Integer, primary_key=True, index=True)
    alumno_id = Column(Integer, ForeignKey("alumno.alumno_id"), nullable=False)
    thread_id = Column(String(255), ForeignKey("thread.id"),nullable=False)
    iniciada_en = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    finalizada_en = Column(DateTime(timezone=True), nullable=True)

    alumno = relationship("Alumno", back_populates="sesiones")
    thread = relationship("Thread", back_populates="sesiones")