from config.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from models.thread_asistente import thread_asistente

class Asistente(Base):
    __tablename__ = "asistente"

    asistente_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    instructions = Column(Text, nullable = False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    
    threads = relationship("Thread", secondary=thread_asistente, back_populates="asistentes")

    def __repr__(self):
        return f"<Asistente(asistente_id={self.asistente_id}, name='{self.name}')>"
