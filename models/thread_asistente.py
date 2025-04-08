from sqlalchemy import Table, Column, Integer, ForeignKey
from config.db_config import Base

thread_asistente = Table(
    "thread_asistente",
    Base.metadata,
    Column("thread_id", Integer, ForeignKey("threads.thread_id"), primary_key=True),
    Column("asistente_id", Integer, ForeignKey("asistentes.asistente_id"), primary_key=True)
)