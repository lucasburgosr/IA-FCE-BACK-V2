from fastapi import APIRouter, Depends
from config.db_config import get_db
from sqlalchemy.orm import Session
from pydantic import EmailStr, BaseModel
from services.auth_service import AuthService
from schemas.login_schema import LoginInput, LoginResponse

router = APIRouter (
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
async def register_alumnos(register_data: dict, db: Session = Depends(get_db)) -> dict:
    service = AuthService(db)
    usuario = await service.registrar_alumnos(register_data)
    return usuario

@router.post("/login", response_model=LoginResponse)
async def iniciar_sesion(login_data: LoginInput, db: Session = Depends(get_db)) -> dict:
    service = AuthService(db)
    usuario = await service.iniciar_sesion(login_data)
    return usuario