# usuario_repository.py
from sqlalchemy.orm import Session
from models.usuario import Usuario
from typing import Optional

class UsuarioRepository:
    def __init__(self, db: Session):
        self.db = db

    """ def get_by_email(self, email: str) -> Optional[Usuario]:
        return self.db.query(Usuario).filter(Usuario.email == email).first() """