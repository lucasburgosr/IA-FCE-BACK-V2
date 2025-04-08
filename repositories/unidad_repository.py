from sqlalchemy.orm import Session
from models.unidad import Unidad

class UnidadRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_id(self, unidad_id: int) -> Unidad:
        return self.db.query(Unidad).filter(Unidad.unidad_id == unidad_id).first()
    
    def get_all(self) -> list[Unidad]:
        return self.db.query(Unidad).all()
    
    def create(self, unidad_data: dict) -> Unidad:
        nueva_unidad = Unidad(**unidad_data)
        self.db.add(nueva_unidad)
        self.db.commit()
        self.db.refresh(nueva_unidad)
        return nueva_unidad
    
    def update(self, unidad: Unidad, update_data: dict) -> Unidad:
        for key, value in update_data.items():
            setattr(unidad, key, value)
        self.db.commit()
        self.db.refresh(unidad)
        return unidad
    
    def delete(self, unidad: Unidad) -> None:
        self.db.delete(unidad)
        self.db.commit()