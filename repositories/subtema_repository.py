from sqlalchemy.orm import Session
from models.subtema import Subtema

class SubtemaRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_id(self, subtema_id: int) -> Subtema:
        return self.db.query(Subtema).filter(Subtema.subtema_id == subtema_id).first()
    
    def get_all(self) -> list[Subtema]:
        return self.db.query(Subtema).all()
    
    def create(self, subtema_data: dict) -> Subtema:
        nuevo_subtema = Subtema(**subtema_data)
        self.db.add(nuevo_subtema)
        self.db.commit()
        self.db.refresh(nuevo_subtema)
        return nuevo_subtema
    
    def update(self, subtema: Subtema, update_data: dict) -> Subtema:
        for key, value in update_data.items():
            setattr(subtema, key, value)
        self.db.commit()
        self.db.refresh(subtema)
        return subtema
    
    def delete(self, subtema: Subtema) -> None:
        self.db.delete(subtema)
        self.db.commit()