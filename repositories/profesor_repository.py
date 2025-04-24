from sqlalchemy.orm import Session
from models.profesor import Profesor
from repositories.usuario_repository import UsuarioRepository
from models.alumno import Alumno
from models.asistente import Asistente

class ProfesorRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_id(self, profesor_id: int) -> Profesor:
        return self.db.query(Profesor).filter(Profesor.profesor_id == profesor_id).first()
    
    def get_all(self) -> list[Profesor]:
        return self.db.query(Profesor).all()
    
    def create(self, profesor_data: dict) -> Profesor:
        nuevo_profesor = Profesor(**profesor_data)
        self.db(nuevo_profesor)
        self.db.commit()
        self.db.refresh(nuevo_profesor)
        return nuevo_profesor
    
    def update(self, profesor: Profesor, update_data: dict) -> Profesor:
        for key, value in update_data.items():
            setattr(profesor, key, value)
        self.db.commit()
        self.db.refresh(profesor)
        return profesor
    
    def delete(self, profesor: Profesor) -> None:
        self.db.delete(profesor)
        self.db.commit()
    
    def get_estudiantes(self, profesor_id: int) -> list[Alumno]:

        profesor = (
            self.db.query(Profesor)
                   .filter_by(profesor_id=profesor_id)
                   .one_or_none()
        )
        if not profesor:
            return []

        mat_id = profesor.materia_id

        alumnos = (
            self.db.query(Alumno)
                   .join(Alumno.asistentes)                    # alumno_asistente + asistentes
                   .filter(Asistente.materia_id == mat_id)    # solo asistentes de su materia
                   .distinct()
                   .all()
        )
        return alumnos
        