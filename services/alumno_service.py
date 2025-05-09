from repositories.alumno_repository import AlumnoRepository
from typing import Dict, Any, List
from models.alumno import Alumno
from sqlalchemy.orm import Session

class AlumnoService:
    def __init__(self, db: Session):
        self.db = db
        self.alumno_repo = AlumnoRepository(db)

    def get_alumno_by_id(self, id: int) -> Alumno:
        alumno = self.alumno_repo.get_by_id(id)
        if not alumno:
            raise ValueError(f"Alumno con id {id} no encontrado")
        return alumno

    def get_alumno_by_email(self, email: str) -> Alumno:
        alumno = self.alumno_repo.get_by_email(email)
        if not alumno:
            raise ValueError(f"Alumno con id {id} no encontrado")
        return alumno

    def get_all_alumnos(self) -> List[Alumno]:
        return self.alumno_repo.get_all()

    def create_alumno(self, alumno_data: Dict[str, Any]) -> Alumno:
        # Agregar validaciones para comprobar que el alumno no esté registrado.
        return self.alumno_repo.create(alumno_data)

    def update_alumno(self, id: int, update_data: Dict[str, Any]) -> Alumno:
        alumno = self.alumno_repo.get_by_id(id)
        # Agregar lógica de validación o transformación de datos de ser necesario.
        return self.alumno_repo.update(alumno, update_data)

    def delete_alumno(self, id: int) -> None:
        alumno = self.alumno_repo.get_by_id(id)
        self.alumno_repo.delete(alumno)

    def increment_message_count(self, alumno_id: int, n: int = 1):
        alumno = self.alumno_repo.get_by_id(alumno_id)
        alumno.mensajes_enviados += n
        self.db.commit()
        self.db.refresh(alumno)
        return alumno
