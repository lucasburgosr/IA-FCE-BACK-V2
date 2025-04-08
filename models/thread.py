from config.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from models import thread_asistente

class Thread(Base):
    __tablename__ = "threads"

    thread_id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    started_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    # Clave foránea a Alumno
    id = Column(Integer, ForeignKey("alumnos.id"), nullable=False)
    alumno = relationship("Alumno", back_populates="threads")

    # Relación con la tabla intermedia ThreadAsistente
    asistentes = relationship("Asistente", secondary=thread_asistente, back_populates="threads")

    def __repr__(self):
        return f"<Thread(thread_id={self.thread_id}, title='{self.title}')>"