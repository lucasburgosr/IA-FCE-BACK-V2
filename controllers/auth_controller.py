from fastapi import APIRouter, Depends
from config.db_config import get_db
from sqlalchemy.orm import Session
from services.auth_service import AuthService

router = APIRouter (
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
async def register_alumnos(register_data: dict, db: Session = Depends(get_db)) -> dict:
    service = AuthService(db)
    usuario = await service.registrar_alumnos(register_data)
    return usuario