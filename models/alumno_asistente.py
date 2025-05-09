from sqlalchemy import Table, Column, Integer, ForeignKey, String
from config.db_config import Base

# Tabla intermedia entre Alumno y Asistente
alumno_asistente = Table(
    'alumno_asistente',
    Base.metadata,
    Column('id', Integer, ForeignKey('alumno.alumno_id'), primary_key=True),
    Column('asistente_id', String, ForeignKey('asistente.asistente_id'), primary_key=True)
)
