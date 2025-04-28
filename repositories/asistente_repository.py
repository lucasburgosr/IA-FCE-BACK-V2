from sqlalchemy.orm import Session
from models.asistente import Asistente

""" Clase repository para interactuar con la DB.

Tener en cuenta que en la app trabajamos con dos objetos Asistente:
- uno que viene de la base de datos (el definido por el modelo) para establecer relaciones que no existen en la API y 
desarrollar funcionalidades específicas
- otro que viene desde la API de OpenAI y tiene más parámetros y funcionalidades propias de la API de Asistentes.

Este repositorio solo gestiona el primero de ellos.  """

class AsistenteRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def get_by_id(self, asistente_id: str):
        return self.db.query(Asistente).filter(Asistente.asistente_id == asistente_id).first()

    def get_all(self) -> list[Asistente]:
        return self.db.query(Asistente).all()
    
    def create(self, asistente_data: dict) -> Asistente:
        asistente = Asistente(**asistente_data)
        self.db.add(asistente)
        self.db.commit()
        self.db.refresh(asistente)
        return asistente
    
    def update(self, asistente: Asistente, nueva_data: dict) -> Asistente:
        for key, value in nueva_data.items():
            setattr(asistente, key, value)
        self.db.commit()
        self.db.refresh(asistente)
        return asistente
    
    def delete(self, asistente: Asistente) -> None:
        self.db.delete(asistente)
        self.db.commit()