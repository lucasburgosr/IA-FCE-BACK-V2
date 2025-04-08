from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from usuario import Usuario

class Profesor(Usuario):
    __tablename__ = "profesores"

    id = Column(Integer, ForeignKey("usuarios.id"), primary_key=True)
    materia_id = Column(Integer, ForeignKey("materias.materia_id"), nullable=False)

    materia = relationship("Materia", back_populates="profesores")

    def __repr__(self):
        return f"<Profesor(profesor_id={self.id}, email='{self.email}')>"