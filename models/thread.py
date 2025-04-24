from config.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from models.thread_asistente import thread_asistente

class Thread(Base):
    __tablename__ = "thread"

    thread_id = Column(String(100), primary_key=True, index=True)
    title = Column(String(255), nullable=True)
    started_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    # Relaciones
    alumno_id = Column(Integer, ForeignKey("alumno.alumno_id"), nullable=False)
    asistentes = relationship("Asistente", secondary=thread_asistente, back_populates="threads")
    sesiones = relationship("SesionChat", back_populates="thread", cascade="all, delete-orphan")


    def __repr__(self):
        return f"<Thread(thread_id={self.thread_id}, title='{self.title}')>"