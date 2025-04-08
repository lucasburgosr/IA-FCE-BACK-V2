from pydantic import BaseModel, EmailStr

class LoginBase(BaseModel):
    email: EmailStr
    password: str

class LoginOut(BaseModel):
    email: EmailStr
    usuario_id: int
    token: str