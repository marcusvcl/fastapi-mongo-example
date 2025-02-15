from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    age: int = Field(..., gt=0, lt=120)
    password: str = Field(..., min_length=6)

    class Config:
        json_schema_extra = {
            "example": {
                "name": "João Silva",
                "email": "joao@example.com",
                "age": 30,
                "password": "senhasecreta"
            }
        }


class UserResponse(UserCreate):
    id: str

    class Config:
        json_schema_extra = {
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "name": "João Silva",
                "email": "joao@example.com",
                "age": 30,
                "password": "senhasecreta"
            }
        }


class UserUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    age: Optional[int] = Field(None, gt=0, lt=120)
    password: Optional[str] = Field(None, min_length=6)

    class Config:
        schema_extra = {
            "example": {
                "name": "João Silva Atualizado",
                "email": "novoemail@example.com",
                "age": 31,
                "password": "novasenha"
            }
        }
