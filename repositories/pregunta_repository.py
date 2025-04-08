from sqlalchemy.orm import Session
from models.pregunta import Pregunta

class PreguntaRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_id(self, pregunta_id: int) -> Pregunta:
        return self.db.query(Pregunta).filter(Pregunta.pregunta_id == pregunta_id).first()
    
    def get_all(self) -> list[Pregunta]:
        return self.db.query(Pregunta).all()
    
    def create(self, pregunta_data: dict) -> Pregunta:
        nueva_pregunta = Pregunta(**pregunta_data)
        self.db.add(nueva_pregunta)
        self.db.commit()
        self.db.refresh(nueva_pregunta)
        return nueva_pregunta
    
    def update(self, pregunta: Pregunta, update_data: dict) -> Pregunta:
        for key, value in update_data.items():
            setattr(pregunta, key, value)
        self.db.commit()
        self.db.refresh(pregunta)
        return pregunta
    
    def delete(self, pregunta: Pregunta) -> None:
        self.db.delete(pregunta)
        self.db.commit()