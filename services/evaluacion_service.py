from sqlalchemy.orm import Session
from typing import Dict, Any, List
from models.evaluacion import Evaluacion
from repositories.evaluacion_repository import EvaluacionRepository

class EvaluacionService:
    def __init__(self, db: Session):
        self.db = db
        self.evaluacion_repo = EvaluacionRepository(db)
        
    def get_evaluacion_by_id(self, evaluacion_id: int) -> Evaluacion:
        evaluacion = self.evaluacion_repo.get_by_id(evaluacion_id)
        if not evaluacion:
            raise ValueError(f"Evaluación con id {evaluacion_id} no encontrada")
        return evaluacion
    
    def get_all_evaluaciones(self) -> List[Evaluacion]:
        return self.evaluacion_repo.get_all()
    
    def create_evaluacion(self, evaluacion_data: Dict[str, Any]) -> Evaluacion:
        # Validaciones
        return self.evaluacion_repo.create(evaluacion_data)
    
    def update_evaluacion(self, evaluacion_id: int, update_data: Dict[str, Any]) -> Evaluacion:
        evaluacion = self.evaluacion_repo.get_by_id(evaluacion_id)
        # Agregar lógica de validación o transformación de datos de ser necesario.
        return self.evaluacion_repo.update(evaluacion, update_data)
    
    def delete_evaluacion(self, evaluacion_id: int) -> None:
        evaluacion = self.evaluacion_repo.get_by_id(evaluacion_id)
        self.evaluacion_repo.delete(evaluacion)