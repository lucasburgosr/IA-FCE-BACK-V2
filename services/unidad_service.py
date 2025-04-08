from repositories.unidad_repository import UnidadRepository
from typing import Dict, Any, List
from models.unidad import Unidad
from sqlalchemy.orm import Session

class UnidadService: 
    def __init__(self, db: Session):
        self.db = db
        self.unidad_repo = UnidadRepository(db)
        
    def get_unidad_by_id(self, unidad_id: int) -> Unidad:
        unidad = self.unidad_repo.get_by_id(unidad_id)
        if not unidad:
            raise ValueError(f"Unidad con id {unidad_id} no encontrado")
        return unidad
    
    def get_all_unidades(self) -> List[Unidad]:
        return self.unidad_repo.get_all()
    
    def create_unidad(self, unidad_data: Dict[str, Any]) -> Unidad:
        # Agregar validaciones para comprobar que el unidad no esté registrado.
        return self.unidad_repo.create(unidad_data)
    
    def update_unidad(self, unidad_id: int, update_data: Dict[str, Any]) -> Unidad:
        unidad = self.unidad_repo.get_by_id(unidad_id)
        # Agregar lógica de validación o transformación de datos de ser necesario.
        return self.unidad_repo.update(unidad, update_data)
    
    def delete_unidad(self, unidad_id: int) -> None:
        unidad = self.unidad_repo.get_by_id(unidad_id)
        self.unidad_repo.delete(unidad)