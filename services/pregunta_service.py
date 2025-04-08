from repositories.pregunta_repository import PreguntaRepository
from typing import Dict, Any, List
from models.pregunta import Pregunta
from sqlalchemy.orm import Session

class PreguntaService: 
    def __init__(self, db: Session):
        self.db = db
        self.pregunta_repo = PreguntaRepository(db)
        
    def get_pregunta_by_id(self, pregunta_id: int) -> Pregunta:
        pregunta = self.pregunta_repo.get_by_id(pregunta_id)
        if not pregunta:
            raise ValueError(f"Pregunta con id {pregunta_id} no encontrado")
        return pregunta
    
    def get_all_preguntas(self) -> List[Pregunta]:
        return self.pregunta_repo.get_all()
    
    def create_pregunta(self, pregunta_data: Dict[str, Any]) -> Pregunta:
        # Agregar validaciones para comprobar que el pregunta no esté registrado.
        return self.pregunta_repo.create(pregunta_data)
    
    def update_pregunta(self, pregunta_id: int, update_data: Dict[str, Any]) -> Pregunta:
        pregunta = self.pregunta_repo.get_by_id(pregunta_id)
        # Agregar lógica de validación o transformación de datos de ser necesario.
        return self.pregunta_repo.update(pregunta, update_data)
    
    def delete_pregunta(self, pregunta_id: int) -> None:
        pregunta = self.pregunta_repo.get_by_id(pregunta_id)
        self.pregunta_repo.delete(pregunta)