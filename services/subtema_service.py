from repositories.subtema_repository import SubtemaRepository
from typing import Dict, Any, List
from models.subtema import Subtema
from sqlalchemy.orm import Session

class SubtemaService: 
    def __init__(self, db: Session):
        self.db = db
        self.subtema_repo = SubtemaRepository(db)
        
    def get_subtema_by_id(self, subtema_id: int) -> Subtema:
        subtema = self.subtema_repo.get_by_id(subtema_id)
        if not subtema:
            raise ValueError(f"Subtema con id {subtema_id} no encontrado")
        return subtema
    
    def get_all_subtemas(self) -> List[Subtema]:
        return self.subtema_repo.get_all()
    
    def create_subtema(self, subtema_data: Dict[str, Any]) -> Subtema:
        # Agregar validaciones para comprobar que el subtema no esté registrado.
        return self.subtema_repo.create(subtema_data)
    
    def update_subtema(self, subtema_id: int, update_data: Dict[str, Any]) -> Subtema:
        subtema = self.subtema_repo.get_by_id(subtema_id)
        # Agregar lógica de validación o transformación de datos de ser necesario.
        return self.subtema_repo.update(subtema, update_data)
    
    def delete_subtema(self, subtema_id: int) -> None:
        subtema = self.subtema_repo.get_by_id(subtema_id)
        self.subtema_repo.delete(subtema)