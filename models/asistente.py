from config.db_config import Base
from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime, timezone
from models.thread_asistente import thread_asistente

class Asistente(Base):
    __tablename__ = "asistente"

    # Atributos del objeto Asistente y sus columnas en la base de datos.
    asistente_id = Column(String(100), primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    instructions = Column(Text, nullable = False)
    created_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=datetime.now(timezone.utc))

    # Indicamos una FK que referencia a un registro en la tabla Materia.
    materia_id = Column(Integer, ForeignKey("materia.materia_id"), nullable=False)
    
    # Establecemos la relación.
    materia = relationship(
        "Materia",
        back_populates="asistente",
    )

    # Establecemos la relación con múltiples Threads. La tabla intermedia 'thread_asistente' gestiona las relaciones.
    threads = relationship("Thread", secondary=thread_asistente, back_populates="asistentes")

    def __repr__(self):
        return f"<Asistente(asistente_id={self.asistente_id}, name='{self.name}')>"
