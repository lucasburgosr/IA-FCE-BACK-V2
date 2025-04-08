from sqlalchemy import Table, Column, Integer, ForeignKey
from config.db_config import Base

alumno_asistente = Table(
    'alumno_asistente',
    Base.metadata,
    Column('id', Integer, ForeignKey('alumnos.id'), primary_key=True),
    Column('asistente_id', Integer, ForeignKey('asistentes.asistente_id'), primary_key=True)
)
