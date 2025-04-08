from sqlalchemy.orm import Session
from models.materia import Materia

class MateriaRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_id(self, materia_id: int) -> Materia:
        return self.db.query(Materia).filter(Materia.materia_id == materia_id).first()
    
    def get_all(self) -> list[Materia]:
        return self.db.query(Materia).all()
    
    def create(self, materia_data: dict) -> Materia:
        nueva_materia = Materia(**materia_data)
        self.db.add(nueva_materia)
        self.db.commit()
        self.db.refresh(nueva_materia)
        return nueva_materia
    
    def update(self, materia: Materia, update_data: dict) -> Materia:
        for key, value in update_data.items():
            setattr(materia, key, value)
        self.db.commit()
        self.db.refresh(materia)
        return materia
    
    def delete(self, materia: Materia) -> None:
        self.db.delete(materia)
        self.db.commit()