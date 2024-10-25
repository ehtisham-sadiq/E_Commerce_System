from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    username: str
    password: str
    email: Optional[EmailStr] = None


class UserLogin(BaseModel):
    username: str
    password: str


class USerOut(BaseModel):
    id: int
    username: str
    email: Optional[EmailStr]


