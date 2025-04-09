from sqlalchemy import Table, Column, Integer, ForeignKey
from config.db_config import Base

thread_asistente = Table(
    "thread_asistente",
    Base.metadata,
    Column("thread_id", Integer, ForeignKey("thread.thread_id"), primary_key=True),
    Column("asistente_id", Integer, ForeignKey("asistente.asistente_id"), primary_key=True)
)