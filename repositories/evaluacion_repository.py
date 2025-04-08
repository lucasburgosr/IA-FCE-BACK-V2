from sqlalchemy.orm import Session
from models.evaluacion import Evaluacion

class EvaluacionRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def get_by_id(self, evaluacion_id: int) -> Evaluacion:
        return self.db.query(Evaluacion).filter(Evaluacion.evaluacion_id == evaluacion_id).first()
    
    def get_all(self) -> list[Evaluacion]:
        return self.db.query(Evaluacion).all()
    
    def create(self, evaluacion_data: dict) -> Evaluacion:
        nueva_evaluacion = Evaluacion(**evaluacion_data)
        self.db.add(nueva_evaluacion)
        self.db.commit()
        self.db.refresh(nueva_evaluacion)
        return nueva_evaluacion
    
    def update(self, evaluacion: Evaluacion, update_data: dict) -> Evaluacion:
        for key, value in update_data.items():
            setattr(evaluacion, key, value)
        self.db.commit()
        self.db.refresh(evaluacion)
        return evaluacion
    
    def delete(self, evaluacion: Evaluacion) -> None:
        self.db.delete(evaluacion)
        self.db.commit()