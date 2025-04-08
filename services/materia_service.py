from repositories.materia_repository import MateriaRepository
from typing import Dict, Any, List
from models.materia import Materia
from sqlalchemy.orm import Session

class MateriaService: 
    def __init__(self, db: Session):
        self.db = db
        self.materia_repo = MateriaRepository(db)
        
    def get_materia_by_id(self, materia_id: int) -> Materia:
        materia = self.materia_repo.get_by_id(materia_id)
        if not materia:
            raise ValueError(f"Materia con id {materia_id} no encontrado")
        return materia
    
    def get_all_materias(self) -> List[Materia]:
        return self.materia_repo.get_all()
    
    def create_materia(self, materia_data: Dict[str, Any]) -> Materia:
        # Agregar validaciones para comprobar que el materia no esté registrado.
        return self.materia_repo.create(materia_data)
    
    def update_materia(self, materia_id: int, update_data: Dict[str, Any]) -> Materia:
        materia = self.materia_repo.get_by_id(materia_id)
        # Agregar lógica de validación o transformación de datos de ser necesario.
        return self.materia_repo.update(materia, update_data)
    
    def delete_materia(self, materia_id: int) -> None:
        materia = self.materia_repo.get_by_id(materia_id)
        self.materia_repo.delete(materia)