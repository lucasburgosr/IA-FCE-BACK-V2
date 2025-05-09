from sqlalchemy.orm import Session
from models.alumno import Alumno

class AlumnoRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, id: int) -> Alumno:
        return self.db.query(Alumno).filter(Alumno.id == id).first()

    def get_all(self) -> list[Alumno]:
        return self.db.query(Alumno).all()
    
    def get_by_email(self, email: str) -> Alumno:
        return self.db.query(Alumno).filter(Alumno.email == email).first()

    def create(self, alumno_data: dict) -> Alumno:
        nuevo_alumno = Alumno(**alumno_data)
        self.db.add(nuevo_alumno)
        self.db.commit()
        self.db.refresh(nuevo_alumno)
        return nuevo_alumno

    def update(self, alumno: Alumno, update_data: dict) -> Alumno:
        for key, value in update_data.items():
            setattr(alumno, key, value)
        self.db.commit()
        self.db.refresh(alumno)
        return alumno

    def delete(self, alumno: Alumno) -> None:
        self.db.delete(alumno)
        self.db.commit()