from repositories.profesor_repository import ProfesorRepository
from typing import Dict, Any, List
from models.profesor import Profesor
from sqlalchemy.orm import Session

class ProfesorService: 
    def __init__(self, db: Session):
        self.db = db
        self.profesor_repo = ProfesorRepository(db)
        
    def get_profesor_by_id(self, profesor_id: int) -> Profesor:
        profesor = self.profesor_repo.get_by_id(profesor_id)
        if not profesor:
            raise ValueError(f"Profesor con id {profesor_id} no encontrado")
        return profesor
    
    def get_all_profesores(self) -> List[Profesor]:
        return self.profesor_repo.get_all()
    
    def create_profesor(self, profesor_data: Dict[str, Any]) -> Profesor:
        # Agregar validaciones para comprobar que el profesor no esté registrado.
        return self.profesor_repo.create(profesor_data)
    
    def update_profesor(self, profesor_id: int, update_data: Dict[str, Any]) -> Profesor:
        profesor = self.profesor_repo.get_by_id(profesor_id)
        # Agregar lógica de validación o transformación de datos de ser necesario.
        return self.profesor_repo.update(profesor, update_data)
    
    def delete_profesor(self, profesor_id: int) -> None:
        profesor = self.profesor_repo.get_by_id(profesor_id)
        self.profesor_repo.delete(profesor)