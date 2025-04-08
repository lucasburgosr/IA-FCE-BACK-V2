from repositories.asistente_repository import AsistenteRepository
from models.asistente import Asistente
from typing import Dict, Any, List
from sqlalchemy.orm import Session
from openai import OpenAI

client = OpenAI()

class AsistenteService:
    def __init__(self, db: Session):
        self.db = db
        self.asistente_repo = AsistenteRepository(db)
        
    def get_asistente_by_id(self, asistente_id: int) -> Asistente:
        asistente = client.beta.assistants.retrieve(asistente_id)
        if not asistente:
            raise ValueError(f"Asistente con el id {asistente_id} no encontrado")
        return asistente
    
    def get_all_asistentes(self) -> List[Asistente]:
        return self.asistente_repo.get_all()
        
    def create_asistentes(self, asistente_data: Dict[str, Any]) -> Asistente:
        
        asistente = client.beta.assistants.create(
            model= "o3-mini",
            instructions=asistente_data.get("instrucciones"),
            name=asistente_data.get("nombre")
        )

        asistente_db = self.asistente_repo.create(asistente)
    
    def update_asistente(self, asistente_id: int, update_data: Dict[str, Any]) -> Asistente:
        asistente = self.asistente_repo.get_by_id(asistente_id)
        return self.asistente_repo.update(asistente, update_data)
    
    def delete_asistente(self, asistente_id: int) -> None:
        asistente = self.asistente_repo.get_by_id(asistente_id)
        self.asistente_repo.delete(asistente)