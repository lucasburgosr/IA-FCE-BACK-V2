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
        
    def get_asistente_by_id(self, asistente_id: str) -> Asistente:
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
    
    def update_asistente(self, asistente_id: str, update_data: Dict[str, Any]) -> dict:
        # 1. Actualizar en OpenAI
        asistente_api = client.beta.assistants.update(
            assistant_id=asistente_id,
            instructions=update_data.get("instructions"),
            name=update_data.get("nombre")  # alias inverso
        )

        # 2. Actualizar en base de datos
        asistente_db = self.asistente_repo.get_by_id(asistente_id)
        if not asistente_db:
            raise ValueError(f"Asistente con id {asistente_id} no encontrado en la base de datos.")

        nueva_data = {}
        if "nombre" in update_data:
            nueva_data["nombre"] = update_data["nombre"]
        if "instructions" in update_data:
            nueva_data["instructions"] = update_data["instructions"]

        self.asistente_repo.update(asistente_db, nueva_data)

        # 3. Devolver datos mapeados al esquema de salida
        return {
            "asistente_id": asistente_api.id,
            "name": asistente_api.name,
            "instructions": asistente_api.instructions,
        }


    
    def delete_asistente(self, asistente_id: str) -> None:
        asistente = self.asistente_repo.get_by_id(asistente_id)
        self.asistente_repo.delete(asistente)